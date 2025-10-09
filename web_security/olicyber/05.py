#!/usr/bin/env python3
import requests

cookies = {
    "password": "admin"
}


result = requests.get("http://web-05.challs.olicyber.it/flag", cookies=cookies)
print(result.status_code)
print(result.headers)
print(result.text)