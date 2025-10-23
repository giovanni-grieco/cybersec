import requests

url = "http://gabibbo-says.challs.olicyber.it/"

# Facciamo una post

data = {
    "gabibbo" : "angry"
}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text)