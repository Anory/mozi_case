import time
import pymysql
import requests
import websocket
import threading
import datetime

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


# class ThreadTest(threading.Thread):
#     def __init__(self, username, token_lists):
#         threading.Thread.__init__(self)
#         self.username = username
#         self.token_lists = token_lists

def get_response(username):
    for account in username:
        # ws = websocket.WebSocket()
        data = {
            "account": account,
            "password": "123456"
        }
        print("\033[0;31;40m\t用户登录所用用户名\033[0m", account)
        start_time = time.time()
        print("开始请求时间 -------------------------------", start_time)
        res = requests.post(url="http://api-robot.mozi.local/v1/user/login", data=data).json()
        # name = res['data']['username']
        # print("用户成功登录的返回的用户名***********", name)
        # token = res['data']['token']
        # print(token)
        # # time.sleep(1)
        # self.token_lists.insert(0, token)
        # file = open('../data/token.txt', 'w')
        # file.write(str(self.token_lists))
        # file.close()
        # ws.connect("ws://10.0.3.31:16050/websocket/{0}/1000".format(token))
        # if ws.connected:
        #     result = ws.recv()
        #     print("链接返回的结果：", result)
            # ws.close()


if __name__ == "__main__":
    # start_time = time.localtime()
    # beijing_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
    # print("111111111", beijing_time)
    t_list = []
    t1 = threading.Thread(target=get_response, args=(name_list,))
    t2 = threading.Thread(target=get_response, args=(name_list,))
    t3 = threading.Thread(target=get_response, args=(name_list,))  # args传入函数所需要的参数
    t_list.append(t1)
    t_list.append(t2)
    t_list.append(t3)
    t1.start()
    t2.start()
    t3.start()
    for t in t_list:  # 等待所有线程完成
        t.join()







