# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import argparse
from .ip_info import get_ip_info, format_ip_info


def main():
    parser = argparse.ArgumentParser(description='Get information about an IP address')
    parser.add_argument('--ip', type=str, help='IP address to look up', required=False)

    args = parser.parse_args()

    if args.ip:
        ip_address = args.ip
    else:
        ip_address = input("Please enter an IP address (or press Enter for your current IP): ").strip() or None

    try:
        ip_info = get_ip_info(ip_address)
        print("\nIP Information:")
        print(format_ip_info(ip_info))
    except ValueError as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == '__main__':
    main()
