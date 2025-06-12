# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Smart IP info - A simple tool to get information about IP addresses."""
from smart_ip_info.ip_info import get_ip_info, format_ip_info
from services import IPInfoService
__version__ = '0.1.3'
__author__ = 'A.A. Suvorov'
__email__ = 'smartlegiondev@gmail.com'
__all__ = [
    "get_ip_info",
    "format_ip_info",
    "IPInfoService",
]
