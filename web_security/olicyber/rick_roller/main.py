import requests

url = "http://roller.challs.olicyber.it/get_flag.php"

response = requests.get(url, allow_redirects=False)
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.text)