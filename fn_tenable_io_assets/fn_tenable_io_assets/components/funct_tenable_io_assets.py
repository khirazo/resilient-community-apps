# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon
from fn_tenable_io_assets.util.tenable_io_lib import call_tenable_io
from pprint import pformat

PACKAGE_NAME = "fn_tenable_io_assets"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'tenable_io_assets''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("tenable_io_assets")
    def _tenable_io_assets_function(self, event, *args, **kwargs):
        """
        Function: Function for multiple operations:
            - Gets Asset data from Tenable.io.
            - Invoke Tenable.io Vulnerability scan for the Asset(s).
        in:
            tio_operation_type: 'search', 'scan', 'scan_status'
            tio_ip_addr: an IP address or comma separated addresses
            tio_severity: comma separated list of Info, Low, Medium, High, Critical combination
            tio_asset_age: asset age in days to retrieve
            tio_scan_name: scan name to override the default scan name in app.config
        out: results dict.
            See ../util/tenable_io.py for more detail
        """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'tenable_io_assets' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            tio_operation_type = kwargs.get("tio_operation_type")  # text
            tio_ip_addr = kwargs.get("tio_ip_addr")  # text
            tio_severity = kwargs.get("tio_severity")  # text
            tio_asset_age = kwargs.get("tio_asset_age")  # number
            tio_scan_name = kwargs.get("tio_scan_name")  # text

            log = logging.getLogger(__name__)
            # debug purpose (note: this exposes access_key and secret_key in the log)
            log.debug("parameters from app.config:")
            log.debug(pformat(self.options))
            
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("tio_operation_type: %s", tio_operation_type)
            log.info("tio_ip_addr: %s", tio_ip_addr)
            log.info("tio_severity: %s", tio_severity)
            log.info("tio_asset_age: %s", tio_asset_age)
            log.info("tio_scan_name: %s", tio_scan_name)

            # create RequestsCommon
            req_common = RequestsCommon(opts=self.opts, function_opts=self.options)
            results = call_tenable_io(self.options, req_common, tio_operation_type,
                                      ip_addr=tio_ip_addr, severity=tio_severity,
                                      asset_age=tio_asset_age, scan_name=tio_scan_name) 
            yield StatusMessage("Finished 'tenable_io_assets' that was running in workflow '{0}'".format(wf_instance_id))

            if results.get('state') != 'Success':
                raise ConnectionError("Tenable.io Error: {0}".format(results.get('reason')))
            else:
                if tio_operation_type.lower() == 'search':
                    yield StatusMessage("{0} assets were returned from Tenable.io".format(results.get('size')))
                else:
                    yield StatusMessage("Tenable.io operation: {0}".format(pformat(results)))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as e:
            yield FunctionError(e)
