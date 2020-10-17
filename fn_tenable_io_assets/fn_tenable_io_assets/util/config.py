# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_tenable_io_assets"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_tenable_io_assets when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_tenable_io_assets]
host_name=cloud.tenable.com
access_key=<tenable.io access key>
secret_key=<tenable.io secret key>
default_scan_name=<default_scan_name>
tio_ui_type=[ classic | new ]
"""
    return config_data
