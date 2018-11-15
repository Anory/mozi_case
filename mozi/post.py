import requests

data = {
    'username': '132364',
    'password': '123456'
}
res = requests.post(url='http://127.0.0.1:8000/login', data=data)
print(res.json())
