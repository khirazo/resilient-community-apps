# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
'''
Created on 2020/10/03

Common lib for QRadar Assets API call
'''
from datetime import datetime
import base64, json

Q_API_ASSETS = "https://{0}/api/asset_model/assets"
Q_UI_ASSET = "https://{0}/console/do/assetprofile/AssetDetails?dispatch=viewAssetDetails&assetId={1}&listName=vulnList"
Q_FLT_IP_ADDR = 'interfaces(ip_addresses(value)) in ({0})'
Q_FLT_VULN_CNT = "vulnerability_count {0}"
Q_FLT_CVSS_SUM = "risk_score_sum {0}"
DEFAULT_RANGE = '0-49'

HTTP_OK = 200

def get_qradar_auth_headers(config):
    headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json' }
    if config.get('username') and config.get('password'):
        ba = base64.b64encode((config.get('username') + ":" + config.get('password')).encode('utf-8'))
        headers['Authorization'] = "Basic " + ba.decode('utf-8')
    elif config.get('authtoken'):
        headers['SEC'] = config.get('authtoken')
    return headers

def get_ip_addr_filter(comma_separated_ip_list):
    ip_addrs = comma_separated_ip_list.split(',')
    quoted_ip_addrs = [] 
    for line in ip_addrs:
        quoted_ip_addrs.append('"{0}"'.format(line.strip()))
    return Q_FLT_IP_ADDR.format(",".join(quoted_ip_addrs))

def get_cvss_sum_filter(cvss_sum):
    return Q_FLT_CVSS_SUM.format(cvss_sum)

def get_vuln_count_filter(vuln_count):
    return Q_FLT_VULN_CNT.format(vuln_count)

def execute_qradar_query(config, req_common, asset_filter, result_range = DEFAULT_RANGE):
    """
    in:
        asset_filter: QRadar Assets filter expression, one of the following:
            One or more (, separated) IP addresses
            Aggregated CVSS. example: >10
            Vulnerability count. example: >5
        result_range:
            0-49, etc
    out: results dict
        state: Success, Failed
        code: Status code from the QRadar REST API endpoint
        reason: Failed reason
        content: assets array of dict
        content_range: 0-1/2, etc
    """
    try:
        headers = get_qradar_auth_headers(config)
        headers['Range'] = "items={0}".format(result_range if result_range else DEFAULT_RANGE)
        params = { 'filter': asset_filter }
        r = req_common.execute_call_v2('GET', Q_API_ASSETS.format(config.get('host')),
                                        headers=headers, params=params,
                                        verify=config.get('verify_cert'))
        if r.status_code == HTTP_OK:
            buf = r.headers.get('content-range')
            content_range = buf[buf.find(' ')+1:] if buf else None
            assets = json.loads(r.text)
            content = reformat_assets(config, assets)
            return {
                'state': 'Success',
                'code': r.status_code,
                'content': content,
                'content_range': content_range
            }
        else:
            return {
                'state': 'Failed',
                'code': r.status_code,
                'reason': r.reason
            }
    except Exception as e:
        return {
            'state': 'Failed',
            'reason': e
        }

def reformat_assets(config, assets):
    '''
    in: QRadar Assets API JSON output
    out: Reformatted Asset JSON
        Asset Keys = [ 'id', 'asset_url', 'interfaces', 'hostnames', 'given_name', 'asset_name',
            'aggregated_cvss', 'vulnerability_count', 'users' ]
    '''
    out_assets = []

    for asset in assets:
        out_asset = {}
        
        out_asset['id'] = asset.get('id')
        out_asset['asset_url'] = Q_UI_ASSET.format(config.get('host'), asset.get('id'))
        out_asset['aggregated_cvss'] = asset.get('risk_score_sum')
        out_asset['vulnerability_count'] = asset.get('vulnerability_count')
        # get interfaces information: ip & mac
        intfs = asset.get('interfaces')
        if intfs:
            out_intfs = []
            for intf in intfs:
                line = {}
                line['mac'] = intf.get('mac_address')
                ips = []
                for ip in intf.get('ip_addresses'):
                    ips.append(ip.get('value'))
                line['ip'] = '|'.join(ips)            
                out_intfs.append("{0} ({1})".format(line.get('ip'), line.get('mac')))
            out_asset['interfaces'] = "\n".join(out_intfs)
        # get host names: netbios, dns or ip
        hosts = asset.get('hostnames')
        if hosts:
            out_hosts = []
            for host in hosts:
                if host.get('type').upper() == 'NETBIOS':
                    out_hosts.append("{0} (netbios)".format(host.get('name')))
                elif host.get('type').upper() == 'DNS':
                    out_hosts.append("{0} (dns)".format(host.get('name')))
            out_asset['hostnames'] = "\n".join(out_hosts)
        # get values from properties
        props = asset.get('properties')
        if props:
            for prop in props:
                if prop.get('name') == 'Given Name':
                    out_asset['given_name'] = prop.get('value')
                elif prop.get('name') == 'Unified Name':
                    out_asset['asset_name'] = prop.get('value')
        # get user names
        users = asset.get('users')
        if users:
            out_users = []
            tmp_users = []
            for user in users:
                tmp_user = {}
                last_seen_profiler = user.get('last_seen_profiler')
                last_seen_scanner = user.get('last_seen_scanner')
                last_seen = last_seen_profiler if last_seen_profiler else last_seen_scanner
                last_seen_date = datetime.fromtimestamp(int(last_seen)/1000)
                tmp_user['username'] = user.get('username')
                tmp_user['last_seen'] = last_seen_date
                tmp_users.append(tmp_user)

            sorted_users = sorted(tmp_users, key=lambda x:x['last_seen'], reverse=True)
            for sorted_user in sorted_users:
                out_users.append("{0} (last seen: {1})".format(sorted_user.get('username'), sorted_user.get('last_seen')))
            out_asset['users'] = "\n".join(out_users)

        out_assets.append(out_asset)
    
    return out_assets