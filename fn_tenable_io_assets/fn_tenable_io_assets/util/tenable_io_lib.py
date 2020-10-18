# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
'''
Created on 2020/10/17

Common lib for Tenable.io API call (via pyTenable)
'''
from datetime import datetime
from tenable.io import TenableIO
from pprint import pprint, pformat

TIO_RETRIES = 3
TIO_BACKOFF = 10
TIO_CLASSIC_ASSET_URL = "https://{0}/app.html#/dashboards/workbench/assets/{1}/overview" 
TIO_NEW_ASSET_URL = "https://{0}/tio/app.html#/vulnerability-management/dashboards/default/assets/asset-details/{1}/overview"
TIO_CLASSIC_SCAN_URL = "https://{0}/app.html#/scans/reports/{1}/history"
TIO_NEW_SCAN_URL = "https://{0}/tio/app.html#/tools/scans/vuln-scans/scan-grid/folders/all-scans/scan-details/{1}/{2}/history"

def call_tenable_io(config, req_common, tio_ope, **kwargs):
    """
    in:scan_name
        config: config dict
        req_common: resilient lib RequestCommon
        tio_ope: operation types:
            search: search assets with vulnerabilities by IP *or* by severity
            scan: ask Tenable.io to initiate a scan (for the IP addresses or default targets when omitted)
            scan_status: check scan status
        ip_addr: one ore more comma separated ip address(es)
        severity: comma separated list of Info, Low, Medium, High, Critical combination
        asset_age: asset age in days to retrieve
        scan_name: scan name
    out: results dict
        state: Success, Failed
        content: Tenable.io assets (tio_ope = search only)
        size: number of assets returned (tio_ope = search only)
        reason: Failed reason (state = Failed only)
        scan_status: scan status (tio_ope = scan_status only)
        scan_name: scan name (tio_ope = scan|scan_status only)
        scan_uuid: scan uuid (tio_ope = scan only)
        scan_url: scan url for Tenable.io (tio_ope = scan only)
    """
    try:
        # Get the function parameters:
        ip_addr = kwargs.get("ip_addr")  # text
        severity = kwargs.get("severity") # text
        asset_age = kwargs.get("asset_age")  # number 
        scan_name = kwargs.get("scan_name")  # text

        tio = TenableIO(access_key=config.get('access_key'), secret_key=config.get('secret_key'),
                        url="https://"+config.get('host_name'), retries=TIO_RETRIES, backoff=TIO_BACKOFF,
                        proxies=req_common.get_proxies())

        if tio_ope.lower() == 'search':
            filters = []
            if ip_addr:
                filters.append('host.target')
                filters.append('eq')
                filters.append(ip_addr)
            if severity:
                filters.append('severity')
                filters.append('eq')
                filters.append(severity)
#             pprint(filters)
            resp = tio.workbenches.vuln_assets(filters, filter_type="and", age=asset_age)
            return {
                'state': 'Success',
                'content': reformat_assets(config, resp),
                'size': len(resp)
            }
        elif tio_ope.lower() == 'scan':
            scan_name = scan_name if scan_name else config.get('default_scan_name')
            scan_id = get_scan_id_from_name(tio, scan_name)
        
            if scan_id > 0:
                targets = ip_addr.split(',') if ip_addr else None
                resp = tio.scans.launch(scan_id, targets=targets)  # targets is optional
                return {
                    'state': 'Success',
                    'scan_name': scan_name,
                    'scan_uuid': resp,  # uuid
                    'scan_url': get_tio_scan_url(config, scan_id, resp)
                }
            else:
                return {
                    'state': 'Failed',
                    'reason': "Scan id for '{0}' not found".format(scan_name)
                }          
        elif tio_ope.lower() == 'scan_status':
            scan_name = scan_name if scan_name else config.get('default_scan_name')
            scan_id = get_scan_id_from_name(tio, scan_name)
        
            if scan_id > 0:
                resp = tio.scans.status(scan_id)
                return {
                    'state': 'Success',
                    'scan_name': scan_name,
                    'scan_status': resp
                }
            else:
                return {
                    'state': 'Failed',
                    'reason': "Scan id for '{0}' not found".format(scan_name)
                }
        else:
            return {
                'state': 'Failed',
                'reason': "No operation '{0}' found".format(tio_ope)
            }
    except Exception as e:
        return {
            'state': 'Failed',
            'reason': e
        }

def get_scan_id_from_name(tenable_io, name):
    '''
    in: Tenable.io scan name
    out: Tenable.io scan id
    '''
    scan_id = 0;
    for scan in tenable_io.scans.list():
        if scan.get('name') == name:
            scan_id = scan.get('id')
    return scan_id

def reformat_assets(config, assets):
    '''
    in: Tenable.io Assets API output
    out: Reformatted Tenable.io Asset array of dict
        Asset Keys = [ 'id', 'asset_url', 'interfaces', 'hostnames', 'severities', 'last_seen', 'agent_name' ]
    '''
    try:
        out_assets = []
        for asset in assets:
            out_asset = {}
            
            out_asset['id'] = asset.get('id')
            out_asset['asset_url'] = get_tio_asset_url(config, asset.get('id'))
            out_asset['last_seen'] = asset.get('last_seen')
            out_asset['agent_name'] = pformat(asset.get('agent_name'))
            # get interfaces information: ipv4 & ipv6
            intfs = []
            intfs.extend(asset.get('ipv4'))
            intfs.extend(asset.get('ipv6'))
            out_asset['interfaces'] = "\n".join(intfs)
            # get host names: netbios, fqdn
            hosts = []
            for fqdn in asset.get('fqdn'):
                hosts.append("{0} (fqdn)".format(fqdn))
            for nb in asset.get('netbios_name'):
                hosts.append("{0} (netbios)".format(nb))
            out_asset['hostnames'] = "\n".join(hosts)
            # get values for severities
            svs = asset.get('severities')
            if svs:
                severity = {}
                for sv in svs:
                    if sv.get('name') == 'Info':
                        severity['info'] = sv.get('count')
                    elif sv.get('name') == 'Low':
                        severity['low'] = sv.get('count')
                    elif sv.get('name') == 'Medium':
                        severity['medium'] = sv.get('count')
                    elif sv.get('name') == 'High':
                        severity['high'] = sv.get('count')
                    elif sv.get('name') == 'Critical':
                        severity['critical'] = sv.get('count')
                out_asset['severities'] = "Critical: {0}\nHigh: {1}\nMedium: {2}\nLow: {3}\nInfo: {4}".format(
                    severity.get('critical'), severity.get('high'), severity.get('medium'),
                    severity.get('low'), severity.get('info'))
    
            out_assets.append(out_asset)
        return out_assets 
    except Exception as e:
        return [ {
            'state': 'Failed',
            'reason': e
        } ]

def get_tio_asset_url(config, asset_uuid):
    ui_type = config.get("tio_ui_type")  # text

    if ui_type.lower() == 'classic':
        return TIO_CLASSIC_ASSET_URL.format(config.get('host_name'), asset_uuid)
    else:
        return TIO_NEW_ASSET_URL.format(config.get('host_name'), asset_uuid)

def get_tio_scan_url(config, scan_id, scan_uuid):
    ui_type = config.get("tio_ui_type")  # text

    if ui_type.lower() == 'classic':
        return TIO_CLASSIC_SCAN_URL.format(config.get('host_name'), scan_id)
    else:
        return TIO_NEW_SCAN_URL.format(config.get('host_name'), scan_id, scan_uuid)
