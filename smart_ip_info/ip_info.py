# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import urllib.request
import urllib.error
import json
from typing import Optional, Dict, Any


def get_ip_info(ip_address: Optional[str] = None) -> Dict[str, Any]:
    base_url = "http://ip-api.com/json/"
    url = f"{base_url}{ip_address}" if ip_address else base_url
    fields = [
        'status', 'message', 'country', 'countryCode', 'region', 'regionName',
        'city', 'zip', 'lat', 'lon', 'timezone', 'isp', 'org', 'as',
        'mobile', 'proxy', 'hosting', 'query'
    ]
    params = f"?fields={','.join(fields)}"

    try:
        with urllib.request.urlopen(f"{url}{params}", timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

            if data.get('status') == 'fail':
                raise ValueError(data.get('message', 'Unknown error'))

            return data

    except urllib.error.URLError as e:
        raise ValueError(f"Network error: {e.reason}")
    except json.JSONDecodeError:
        raise ValueError("Invalid API response")
    except Exception as e:
        raise ValueError(f"Unexpected error: {str(e)}")


def format_ip_info(ip_info: Dict[str, Any]) -> str:
    if not ip_info or ip_info.get('status') == 'fail':
        return "Failed to get IP information"

    result = []
    mappings = {
        'IP Address': 'query',
        'Country': lambda x: f"{x.get('country')} ({x.get('countryCode')})",
        'Region': lambda x: f"{x.get('regionName')} ({x.get('region')})",
        'City': 'city',
        'ZIP': 'zip',
        'Coordinates': lambda x: f"{x.get('lat')}, {x.get('lon')}",
        'Timezone': 'timezone',
        'ISP': 'isp',
        'Organization': 'org',
        'AS': 'as',
        'Mobile': 'mobile',
        'Proxy': 'proxy',
        'Hosting': 'hosting'
    }

    for name, key in mappings.items():
        try:
            value = key(ip_info) if callable(key) else ip_info.get(key)
            if value not in (None, '', False):
                result.append(f"{name}: {value}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

    return "\n".join(result)
