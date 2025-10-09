#!/usr/bin/env python3

import requests

headers = {
    "X-Password" : "admin"
}

response = requests.get("http://web-03.challs.olicyber.it/flag", headers=headers)
print(response.status_code)
print(response.headers)
print(response.text)