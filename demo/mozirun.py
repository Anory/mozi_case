import requests
import json

url = 'http://api-robot.mozi.local/v1/user/login'


class RunMozi:
    def __init__(self, url=url, method=None, data=None, headers=None):
        self.res = self.run_main(url, method, data, headers)

    def get(self, url, data):
        result = requests.get(url=url, data=data).json()
        return result

    def post(self, url, data, headers):
        result = requests.post(url=url, data=data, headers=headers).json()
        return json.dumps(result, indent=4)

    def run_main(self, url, method, data=None, headers=None):
        result = None
        if method == 'GET':
            res = self.get(url, data)
        else:
            res = self.post(url, data, headers)
        return res


if __name__ == '__main__':
    url = 'http://api-robot.mozi.local/v1/user/login'
    data = {
        'account': 'jies',
        'password': '123456',
        'device_id': '1',
        'os_ver': '1'
    }
    run = RunMozi(url, 'POST', data)
    print(run.res)
