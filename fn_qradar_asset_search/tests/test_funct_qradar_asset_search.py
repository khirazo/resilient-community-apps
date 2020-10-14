# -*- coding: utf-8 -*-
"""
Tests using selftest
    usage: pytest
"""

import pytest
from resilient_lib import RequestsCommon
from fn_qradar_asset_search.util.qradar_assets import execute_qradar_query, get_ip_addr_filter, get_cvss_sum_filter, get_vuln_count_filter  # @UnresolvedImport

PACKAGE_NAME = "fn_qradar_asset_search"

class TestQradarAssetSearch:
    """ Tests for the qradar_asset_search function"""

    opts = {
        'fn_qradar_asset_search': {
            'host': '10.189.123.45',
            'username': None,
            'password': None,
            'authtoken': 'da570c70-83d4-4e0b-8efe-b29ceefa3f99',
            'verify_cert': 'false' 
        }
    }

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

    @pytest.mark.parametrize("asset_type, filter_value, qvm_result_range", [
        ('ip_addr', '0.0.0.0', '0-0'),
        ('cvss_sum', '>=0', '0-10'),
        ('vuln_count', '>=0', '0-5')
    ])
    def test_success(self, asset_type, filter_value, qvm_result_range):
        """ Test calling with sample values for the parameters """
        self.options = self.opts.get(PACKAGE_NAME, {})
        self.get_opts_from_app_config()

        req_common = RequestsCommon(opts=self.opts, function_opts=self.options)

        asset_filter = ""
        if asset_type == 'ip_addr':
            asset_filter = get_ip_addr_filter(filter_value)
        elif asset_type == 'cvss_sum':
            asset_filter = get_cvss_sum_filter(filter_value)
        elif asset_type == 'vuln_count':
            asset_filter = get_vuln_count_filter(filter_value)

        results = execute_qradar_query(self.config, req_common, asset_filter, qvm_result_range)

        assert(results['state'] == "Success")
