import time
import pymysql
import requests
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
# sql = "SELECT username FROM user_info_kaicai WHERE username in('mkij', 'jies')"
mozi_cursor.execute(sql)
name = mozi_cursor.fetchall()  # 获取查询出来的内容
name_list = []
for i in name:
    name_list.append(",".join(list(i)))  # 将获取到的元组类型转换成列表类型


class ThreadTest(threading.Thread):
    def __init__(self, username, token_lists):
        threading.Thread.__init__(self)
        self.username = username
        self.token_lists = token_lists

    def get_response(self):
        for account in self.username:
            ws = websocket.WebSocket()
            data = {
                "account": account,
                "password": "123456"
            }
            print(account)
            res = requests.post(url="http://api-robot.mozi.local/v1/user/login", data=data).json()
            # print(res)
            token = res['data']['token']
            # print(token)
            # time.sleep(1)
            self.token_lists.insert(0, token)  # 将获取到的token存放到列表里面
            # print(self.token_lists)
            file = open('../data/token.txt', 'w')  # 将token_list文件存放到本地的txt文件中
            file.write(str(self.token_lists))
            file.close()
            ws.connect("ws://10.0.3.31:16050/websocket/{0}/1000".format(token))
            if ws.connected:
                result = ws.recv()
                print("链接返回的结果：", result)
                # ws.close()


if __name__ == "__main__":
    token_list = []
    run = ThreadTest(name_list, token_list)
    run.get_response()
    t_list = []
    count = 1
    for i in range(count):
        star_time = time.time()
        print("-------------------------------------")
        print("线程1开始时间：", star_time)
        t1 = threading.Thread(target=run.get_response())
        print("--------------线程分割--------------")
        print("线程2开始时间：", star_time)
        t2 = threading.Thread(target=run.get_response())
        t_list.append(t1)
        t_list.append(t2)
        t1.start()
        t2.start()
    for t in t_list:
        t.join()







