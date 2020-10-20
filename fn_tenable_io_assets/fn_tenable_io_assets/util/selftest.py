# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_tenable_io_assets
"""

import logging
from resilient_lib import RequestsCommon
from fn_tenable_io_assets.util.tenable_io_lib import call_tenable_io
from pprint import pformat

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_tenable_io_assets", {})

    try:       
        req_common = RequestsCommon(opts=opts, function_opts=app_configs)
        results = call_tenable_io(app_configs, req_common, 'search', ip_addr='0.0.0.0') 

        if results.get('state') == 'Success':
            log.info(pformat(results))
            return {"state": "Success"}
        else:
            raise ConnectionError("Could not access Tenable.io Assets: {0}".format(results.get('reason')))

    except Exception as e:
        log.info(str(e))
        return {
            'state': 'Failed',
            'reason': str(e)
        }
