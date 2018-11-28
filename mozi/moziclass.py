import requests
import json

url = 'http://api-robot.mozi.local/v1/user/login'
class RunMain:
    def __init__(self, url=url, method=None, data=None, headers=None):
        self.res = self.run_main(url, method, data, headers)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data, headers):
        res = requests.post(url=url, data=data, headers=headers).json()
        return res

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data, headers)
        return res


if __name__ == '__main__':
    url = "http://192.168.1.191:8181/mozi/v1/extract/coin/onExtractCoin"
    data = {
        'wallet_id': '969',
        'wallet_address': 'BGeLDFoNKoAGecETkDZPvf3xkArpXRGK7e',
        'wallet_name': '我的钱包',
        'trade_num': '10',
        'trade_password': '123456'
    }
    header = {
        'token': '24ce68ffa9afddab639d7a6a6f010f16'
    }
    run = RunMain(url, 'POST', data, header)
    print(run.res)
