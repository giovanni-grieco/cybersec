#!/usr/bin/env python3
import requests

session = requests.Session()

#sets session up
session.get("http://web-06.challs.olicyber.it/token")

result = session.get("http://web-06.challs.olicyber.it/flag")
print(result.status_code)
print(result.headers)
print(result.text)