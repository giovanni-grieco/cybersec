#!/usr/bin/env python3

import requests


params = {
    "id" : "flag"
}

response = requests.get("http://web-02.challs.olicyber.it/server-records", params=params)
print(response.text)
print(response.status_code)