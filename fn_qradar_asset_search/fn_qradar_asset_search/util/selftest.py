# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_qradar_asset_search
"""

import logging
from resilient_lib import RequestsCommon
from pprint import pformat
from fn_qradar_asset_search.util.qradar_assets import execute_qradar_query, get_ip_addr_filter  # @UnresolvedImport

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
# log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_qradar_asset_search", {})
    
    try:
        config = {
            'host': app_configs.get('host'),
            'username': app_configs.get('username'),
            'password': app_configs.get('password'),
            'authtoken': app_configs.get('authtoken') }
        config['verify_cert'] = False if app_configs.get('verify_cert').lower() == 'false' else True
    
        req_common = RequestsCommon(opts=opts, function_opts=app_configs)
        asset_filter = get_ip_addr_filter('0.0.0.0')
        results = execute_qradar_query(config, req_common, asset_filter)

        if results.get('state') == 'Success':
            log.info(pformat(results))
            return {"state": "Success"}
        else:
            raise ConnectionError("QRadar Assets could not be retrieved. {0}: {1}".format(
                results.get('code'), results.get('reason')))

    except Exception as e:
        log.info(str(e))
        return {
            'state': 'Failed',
            'reason': str(e)
        }