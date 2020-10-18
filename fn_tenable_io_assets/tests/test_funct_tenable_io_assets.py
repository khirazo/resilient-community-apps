# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_lib import RequestsCommon
from fn_tenable_io_assets.util.tenable_io_lib import call_tenable_io
from pprint import pprint

PACKAGE_NAME = "fn_tenable_io_assets"

class TestTenableIoAssets:
    """ Tests for the tenable_io_assets function"""

    opts = {
        'fn_tenable_io_assets': {
            'host_name': 'cloud.tenable.com',
            'access_key': '',
            'secret_key': '',
            'default_scan_name': 'MK-LAN',
            'tio_ui_type': 'classic'
        }
    }

    @pytest.mark.parametrize("tio_ope, ip_addr, severity, asset_age, scan_name", [
        ('search', '172.30.34.1,172.30.34.36', None, None, None),
        ('search', '172.30.34.1,172.30.34.36', 'Medium,High,Critical', 120, None),
        ('search', None, 'High,Critical', None, None),
        ('scan_status', None, None, None, 'MK-LAN'),
        ('scan_status', None, None, None, None)
    ])
    def test_success(self, tio_ope, ip_addr, severity, asset_age, scan_name):
        """ Test calling with sample values for the parameters """
        self.config = self.opts.get(PACKAGE_NAME, {})
        req_common = RequestsCommon(opts=self.opts, function_opts=self.config)

        results = call_tenable_io(self.config, req_common, tio_ope, ip_addr=ip_addr, severity=severity, asset_age=asset_age, scan_name=scan_name)
        pprint(results)
        assert(results['state'] == "Success")

    @pytest.mark.parametrize("tio_ope, ip_addr, severity, asset_age, scan_name", [
        ('search', None, None, None, None),
        ('scan_status', None, None, None, 'NO_EXIST')
    ])
    def test_fail(self, tio_ope, ip_addr, severity, asset_age, scan_name):
        """ Test calling with sample values for the parameters """
        self.config = self.opts.get(PACKAGE_NAME, {})
        req_common = RequestsCommon(opts=self.opts, function_opts=self.config)

        results = call_tenable_io(self.config, req_common, tio_ope, ip_addr=ip_addr, severity=severity, asset_age=asset_age, scan_name=scan_name)
        pprint(results)
        assert(results['state'] == "Failed")
