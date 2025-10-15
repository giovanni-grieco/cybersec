#!/usr/bin/env python3
import requests

form={
    "username" : "admin",
    "password" : "admin"
}

#Optional, default is x-www-form-urlencoded
headers={
    "Content-Type" : "application/x-www-form-urlencoded"
}

result = requests.post("http://web-08.challs.olicyber.it/login", data=form, headers=headers)
print(result.status_code)
print(result.headers)
print(result.text)