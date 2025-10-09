#!/usr/bin/env python3
import requests

headers = {
    "Accept" : "application/xml",
    #"Content-Type" : "application/xml" Only for data when we're sending it
}


result = requests.get("http://web-04.challs.olicyber.it/users", headers=headers)
print(result.status_code)
print(result.headers)
print(result.text)