import requests
import json

url: str = "http://too-small-reminder.challs.olicyber.it/"

register_url = url+"register"

login_url = url+"login"

logout_url = url+"logout"

admin_url = url+"admin"

data = {
    "username": "giovanni200111",
    "password": "giovanni200111"
}

session = requests.Session()

response = session.post(register_url, json=data)
print(response.text)

response = session.post(login_url, json=data)
print(response.text)

cookies = session.cookies.get_dict()
print(cookies)

admin_response = session.get(admin_url)
print(admin_response.text)

session_id = cookies.get("session_id")
session = requests.Session()

session.cookies.set("session_id", session_id) # Bisogna resettare la sessione per cambiare il session_id

print(session.cookies.get_dict())
response = session.get(logout_url)
print(response.text)



# Forse possiamo fare bruteforce sull'ID di sessione dell'admin
# Ma magari l'admin non è loggato?
