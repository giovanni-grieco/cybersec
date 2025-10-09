#!/usr/bin/env python3

#CSRF
import requests

session = requests.Session()

headers = {
    "Content-Type": "application/json"
}

data = {
    "username": "admin",
    "password": "admin"
}

response = session.post("http://web-11.challs.olicyber.it/login", json=data, headers=headers)

response_json = response.json()
first_csrf_token = response_json.get("csrf")

flag: str = ""
csrf_token = None



for i in range(4):
    if csrf_token is None:
        csrf_token = first_csrf_token

    params = {
        "index" : i,
        "csrf": csrf_token
    }
    response = session.get("http://web-11.challs.olicyber.it/flag_piece", params=params)
    flag = flag + response.json().get("flag_piece")
    csrf_token = response.json().get("csrf")

print(flag)