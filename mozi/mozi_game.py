import time
import pymysql
import requests
from websocket import create_connection
import websocket
import threading

mozi_connect = pymysql.Connect(
    host='192.168.1.194',
    port=3306,
    user='root',
    passwd='Mz18!@#qwer',
    db='mozi',
    charset='utf8'
)

# 获取游标
mozi_cursor = mozi_connect.cursor()
sql = "SELECT username FROM user_info_kaicai WHERE id BETWEEN 650 AND 2000"
# sql = "SELECT username FROM user_info_kaicai WHERE username in('mkij')"
mozi_cursor.execute(sql)
name = mozi_cursor.fetchall()  # 获取查询出来的内容
name_list = []
for i in name:
    name_list.append(",".join(list(i)))  # 将获取到的元组类型转换成列表类型


class ThreadTest(threading.Thread):
    def __init__(self, username):
        threading.Thread.__init__(self)
        self.username = username

    def get_response(self):
        for account in self.username:
            data = {
                "account": account,
                "password": "123456"
            }
            print(account)
            res = requests.post(url="http://api-robot.mozi.local/v1/user/login", data=data).json()
            # print(res)
            token = res['data']['token']
            # print(token)
            time.sleep(5)
            url = 'ws://10.0.3.21:19090/ws?token={0}'
            while True:  # 一直链接，直到连接上就退出循环
                # time.sleep(0.5)
                try:
                    ws = create_connection(url.format(token))
                    ws.send("{'i':1,'t':123456,'c':'joinRoom','d':{'detailId':1000}}")
                    response = ws.recv()
                    print(response)
                    # print(ws)
                    break
                except Exception as e:
                    print('连接异常：', e)
                    continue
            # while True:  # 连接上，退出第一个循环之后，此循环用于一直获取数据
            #     # time.sleep(0.5)
            #     ws.send("{'i':1,'t':123456,'c':'joinRoom','d':{'detailId':1000}}")
            #     response = ws.recv()
            #     print(response)
            #     break


if __name__ == "__main__":
    run = ThreadTest(name_list)
    run.get_response()
    t_list = []
    for i in range(10):
        start_time = time.time()
        print(start_time)
        t = threading.Thread(target=run.get_response())
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()







