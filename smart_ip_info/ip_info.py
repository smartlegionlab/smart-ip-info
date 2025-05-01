# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import requests


def get_ip_info(ip_address=None):
    url = f"http://ip-api.com/json/{ip_address}" if ip_address else "http://ip-api.com/json/"
    params = {
        'fields': 'status,message,continent,continentCode,country,countryCode,region,regionName,'
                  'city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,'
                  'reverse,mobile,proxy,hosting,query'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get('status') == 'fail':
            raise ValueError(data.get('message', 'Unknown error'))

        return data
    except requests.RequestException as e:
        raise ValueError(f"Error fetching IP info: {str(e)}")


def format_ip_info(ip_info):
    if not ip_info or ip_info.get('status') == 'fail':
        return "Failed to get IP information"

    formatted = []
    fields = [
        ('IP Address', 'query'),
        ('Country', 'country'),
        ('Region', 'regionName'),
        ('City', 'city'),
        ('ZIP Code', 'zip'),
        ('Coordinates', lambda x: f"{x['lat']}, {x['lon']}"),
        ('Timezone', 'timezone'),
        ('ISP', 'isp'),
        ('Organization', 'org'),
        ('AS Number', 'as'),
        ('Mobile', 'mobile'),
        ('Proxy', 'proxy'),
        ('Hosting', 'hosting')
    ]

    for name, key in fields:
        if callable(key):
            value = key(ip_info)
        else:
            value = ip_info.get(key)

        if value not in (None, ''):
            formatted.append(f"{name}: {value}")

    return "\n".join(formatted)
