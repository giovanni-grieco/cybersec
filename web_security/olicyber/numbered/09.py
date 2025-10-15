#!/usr/bin/env python3

import requests

headers = {
    "Content-Type": "application/json",
    "Accept": "application/xml" #Can be ignored by the webserver
}

form_data = {
    "username": "admin",
    "password": "admin"
}



response = requests.post("http://web-09.challs.olicyber.it/login", headers=headers, json=form_data)

print(response.status_code)
print(response.headers)
print(response.text)