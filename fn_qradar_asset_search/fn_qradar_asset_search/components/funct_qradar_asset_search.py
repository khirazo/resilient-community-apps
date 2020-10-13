# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon
from pprint import pformat
from fn_qradar_asset_search.util.qradar_assets import execute_qradar_query, get_ip_addr_filter, get_cvss_sum_filter, get_vuln_count_filter  # @UnresolvedImport

PACKAGE_NAME = "fn_qradar_asset_search"
   
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_asset_search''"""

    def get_opts_from_app_config(self):
        # getting required parameters from app.config
        self.config = {
            'host':self.options.get('host'), 
            'username':self.options.get('username'), 
            'password':self.options.get('password'), 
            'authtoken':self.options.get('authtoken') }
        if self.options.get('verify_cert').lower() == 'false':
            vc = False
        elif self.options.get('verify_cert').lower() == 'true':
            vc = True
        else:
            vc = self.options.get('verify_cert') # when /path/to/certfile is specified
        self.config['verify_cert'] = vc

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        self.get_opts_from_app_config()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        self.get_opts_from_app_config()

    @function("qradar_asset_search")
    def _qradar_asset_search_function(self, event, *args, **kwargs):
        """
        Function: Search QRadar Asset by IP address, by aggregated CVSS score,
            or by vulnerability count
        in:
            qvm_query_type: 'ip_addr', 'cvss_sum', or 'vuln_count'
            qvm_query_value: ip address, aggregated cvss (>100, etc), vulnerability count (>10, etc)
            qvm_result_range: 0-49, etc
        out: results dict
            state: Success, Failed
            code: Status code from the QRadar REST API endpoint
            reason: Failed reason
            content: Reformatted QRadar Asset array of dict:
                Asset Keys = [ 'id', 'asset_url', 'interfaces', 'hostnames', 'given_name',
                    'asset_name', 'aggregated_cvss', 'vulnerability_count', 'users' ]
            content_range: 0-1/2, etc
        """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_asset_search' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            qvm_query_type = kwargs.get("qvm_query_type")  # text
            qvm_query_value = kwargs.get("qvm_query_value")  # text
            qvm_result_range = kwargs.get("qvm_result_range")  # text

            self.log = logging.getLogger(__name__)

            # debug purpose (note: this exposes password or apitoken in the log)
            self.log.debug("parameters from app.config:")
            self.log.debug(pformat(self.config))

            self.log.info("incident_id: %s", incident_id)
            self.log.info("artifact_id: %s", artifact_id)
            self.log.info("qvm_query_type: %s", qvm_query_type)
            self.log.info("qvm_query_value: %s", qvm_query_value)
            self.log.info("qvm_result_range: %s", qvm_result_range)

            # create RequestsCommon
            req_common = RequestsCommon(opts=self.opts, function_opts=self.options)

            if qvm_query_type.lower() == 'ip_addr':
                asset_filter = get_ip_addr_filter(qvm_query_value)
            elif qvm_query_type.lower() == 'cvss_sum':
                asset_filter = get_cvss_sum_filter(qvm_query_value)
            elif qvm_query_type.lower() == 'vuln_count':
                asset_filter = get_vuln_count_filter(qvm_query_value)

            results = execute_qradar_query(self.config, req_common, asset_filter, qvm_result_range)
            yield StatusMessage("Finished 'qradar_asset_search' that was running in workflow '{0}'".format(wf_instance_id))
            
            if results.get('state') != 'Success':
                raise ConnectionError("QRadar Assets could not be retrieved. {0}: {1}".format(
                    results.get('code'), results.get('reason')))
            else:
                yield StatusMessage("{0} assets were returned from QRadar Assets data".format(results.get('content_range')))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as e:
            yield FunctionError(str(e))
