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
    url = 'http://api-robot.mozi.local/v1/user/login'
    data = {
        'account':'jies',
        'password':'123456',
        'device_id':'1',
        'os_ver':'1'
    }
    run = RunMain(url, 'POST', data)
    print(run.res)
