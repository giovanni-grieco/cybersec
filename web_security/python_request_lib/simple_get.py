#!/usr/bin/env python3
import requests



result = requests.get("http://web-01.challs.olicyber.it")
print(result.text)
print(result.status_code)

