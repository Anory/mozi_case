import pymysql
import requests
from websocket import create_connection
import threading
import time


# 链接194测试数据库
mozi_connect = pymysql.Connect(
    host='192.168.1.194',
    port=3306,
    user='root',
    passwd='Mz18!@#qwer',
    db='mozi',
    charset='utf8'
)


# 获取用户名字列表
def get_name_list(sql):
    mozi_cursor = mozi_connect.cursor()  # 建立数据游标
    mozi_cursor.execute(sql)
    name = mozi_cursor.fetchall()  # 获取查询出来的内容
    lists = []
    for i in name:
        lists.append(",".join(list(i)))  # 将获取到的元组类型转换成列表类型
    return lists


# 等待游戏开始
def get_response(username):
    for account in username:
            data = {
                "account": account,
                "password": "123456"
            }
            time.sleep(5)
            # print(account)
            res = requests.post(url="http://api-robot.mozi.local/v1/user/login", data=data).json()
            name = res['data']['username']
            print("登录用户名=================》", name)
            token = res['data']['token']
            # print(token)
            url = 'ws://10.0.3.21:19090/ws?token={0}'
            count = 1
            while True:  # 一直链接，直到连接上就退出循环
                try:
                    ws = create_connection(url.format(token))
                    ws.send("{'i':1,'t':123456,'c':'joinRoom','d':{'detailId':1000}}")
                    response = ws.recv()
                    print(response)
                    break
                except Exception as e:
                    time.sleep(2)
                    print(token)
                    print('连接异常：', e)
                    continue
            # while count < 6:
            #     count += 1
            #     print("aaa:", ws.recv())



if __name__ == "__main__":
    sql = "SELECT username FROM user_info_kaicai WHERE id BETWEEN 650 AND 1000"
    # sql = "SELECT username FROM user_info_kaicai WHERE username in('mkij', 'jies')"
    name_list = get_name_list(sql)
    # run = get_response(name_list)
    t_list = []
    for i in range(1):
        t1 = threading.Thread(target=get_response, args=(name_list,))
        t_list.append(t1)
    for t in t_list:
        t.start()
    for t in t_list:  # 等待所有线程完成
        t.join()







