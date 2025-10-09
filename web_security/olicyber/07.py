#! /usr/bin/env python3

import requests


response = requests.head("http://web-07.challs.olicyber.it/")
print(response.status_code)
print(response.headers)
print(response.text)