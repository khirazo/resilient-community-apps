# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_qradar_asset_search"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_qradar_asset_search when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u'''[fn_qradar_asset_search]
host=qradar_host_or_ip_without_scheme (https:// is implied)
# Either username + password OR authtoken is needed
# Former has precedence, so username/password must be blank to use authtoken)
#username=(optional)qradar_username
#password=(optional)qradar_password OR
authtoken=(optional)auth_service_token
# verify_cert default is true
#verify_cert=[ /path/to/certfile | true (use env) | false ]
'''
    return config_data
