# Smart IP Info <sup>v0.1.3</sup>

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-ip-info)
![PyPI](https://img.shields.io/pypi/v/smart-ip-info)
![PyPI - Downloads](https://img.shields.io/pypi/dm/smart-ip-info?label=pypi%20downloads)
![GitHub License](https://img.shields.io/github/license/smartlegionlab/smart-ip-info)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-ip-info)](https://github.com/smartlegionlab/smart-ip-info/)
[![PyPI - Format](https://img.shields.io/pypi/format/smart-ip-info)](https://pypi.org/project/smart-ip-info)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-ip-info?style=social)](https://github.com/smartlegionlab/smart-ip-info/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-ip-info?style=social)](https://github.com/smartlegionlab/smart-ip-info/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-ip-info?style=social)](https://github.com/smartlegionlab/smart-ip-info/)

A simple command-line tool to get information about IP addresses.

## 🌟 Features

- 100% pure Python (no external dependencies)
- Supports both CLI and programmatic usage
- Fast IP lookup (uses ip-api.com free tier)
- Detailed network information
- Clean, developer-friendly output
- Privacy-focused (no tracking)

## 📦 Installation

```bash
pip install smart-ip-info
```

Or for the latest development version:

```bash
pip install git+https://github.com/smartlegionlab/smart-ip-info.git
```

## 🚀 Usage

### Command Line Interface

Basic usage:
```bash
smart-ip-info --ip 8.8.8.8
```

Interactive mode (prompts for IP):
```bash
smart-ip-info
```

### Python API

```python
from smart_ip_info import get_ip_info, format_ip_info

# Get info about an IP
info = get_ip_info("8.8.8.8")

# Get info about your own IP
my_info = get_ip_info()

# Format results
print(format_ip_info(info))
```

## 📊 Example Output

```plaintext
IP Address: 8.8.8.8
Country: United States (US)
Region: California (CA)
City: Mountain View
ZIP: 94043
Coordinates: 37.4056, -122.0775
Timezone: America/Los_Angeles
ISP: Google LLC
Organization: Google Public DNS
AS: AS15169 Google LLC
Proxy: False
Hosting: True
```
---

## ⚠️ Limitations

- Free tier has 45 requests/minute limit
- No commercial API support (yet)
- IPv6 support is limited

***

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2025, A.A. Suvorov
    All rights reserved.