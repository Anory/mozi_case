import requests
import time
import threading
# import json


def send_post(urls, datas, headers):
    res = requests.post(url=urls, data=datas, headers=headers).json()
    print(res)


if __name__ == "__main__":
    url = "http://192.168.1.191:8181/mozi/v1/extract/coin/onExtractCoin"
    data = {
        'wallet_id': '10219',
        'wallet_address': 'BGeLDFoNKoAGecETkDZPvf3xkArpXRGK7e',
        'wallet_name': '我的钱包',
        'trade_num': '10',
        'trade_password': '123456'
    }
    header = {
        'token': 'bf33e6c7f59011cf8e6353124db21a32'
    }

    data1 = {
        'wallet_id': '969',
        'wallet_address': 'BGeLDFoNKoAGecETkDZPvf3xkArpXRGK7e',
        'wallet_name': '我的钱包',
        'trade_num': '10',
        'trade_password': '423542'
    }

    header1 = {
        'token': '03fa01c4f72f6f1bc3403f54917a4316'
    }

    data2 = {
        'wallet_id': '15',
        'wallet_address': 'BGeLDFoNKoAGecETkDZPvf3xkArpXRGK7e',
        'wallet_name': '我的钱包',
        'trade_num': '10',
        'trade_password': '000000'
    }

    header2 = {
        'token': 'b53a6f1dd554a8b6e33d3d4ee36c548e'
    }
    # run = send_post(url, data, header)
    t_list = []
    for i in range(2000):
        t1 = threading.Thread(target=send_post, args=(url, data, header,))
        t2 = threading.Thread(target=send_post, args=(url, data1, header1,))
        t3 = threading.Thread(target=send_post, args=(url, data2, header2,))
        t_list.append(t1)
        t_list.append(t2)
        t_list.append(t3)
    for t in t_list:
        # start_time = time.time()
        # print(start_time)
        t.start()
    for t in t_list:
        t.join()
