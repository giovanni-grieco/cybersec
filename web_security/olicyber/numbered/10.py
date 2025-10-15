#!/usr/bin/env python3

import requests

response = requests.options("http://web-10.challs.olicyber.it/")
print(response.status_code)
print(response.headers)
print(response.text)

response = requests.put("http://web-10.challs.olicyber.it/")
print(response.status_code)
print(response.headers)
print(response.text)