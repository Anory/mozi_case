import requests
import threading
import time

# 用list存放所有请求的响应时间
post1_times = []
post2_times = []


# 创建线程类
class ThreadTest(threading.Thread):
    def __init__(self, url, data, headers=None):
        threading.Thread.__init__(self)
        self.url = url
        self.data = data
        self.headers = headers

    # POST方法
    def send_post1(self):
        start_time = time.time()
        post1_msg = requests.post(url=self.url, data=self.data)
        end_time = time.time()
        post1_times.append(end_time-start_time)
        return post1_msg

    # GET方法
    def send_post2(self):
        start_time = time.time()
        post2_msg = requests.post(url=self.url, data=self.data, headers=self.headers)
        end_time = time.time()
        post2_times.append(end_time-start_time)
        return post2_msg


# url01 = 'http://api-robot.mozi.local/v1/user/login'
# data01 = {
#     'account': 'mkij',
#     'password': '123456',
#     'device_id': '1',
#     'os_ver': '1'
# }
# test1 = ThreadTest(url01, data01)
# result = test1.send_post1().json()
# token = (result["data"]["token"])
# print(token)

url02 = 'http://192.168.1.191:8181/mozi/v1/assets/transfer/aicBatchCollect'
# data02 = {
#     'toUserId': '1525682336011088',
#     'orderId': '0',
# }
headers = {
    'token': "15d10418f881207fb1000fa2fd64fce3",
}

test2 = ThreadTest(url02, headers)
# print(test2.send_post2().json(), "hahahahah")
j = test2.send_post2().json()  # 将接口放回的信息转换成json格式
msg = (j["code"])
t_list = []
count = 1

# 创建线程
for i in range(count):
    # t1 = threading.Thread(target=test1.send_post1)
    star_time = time.time()
    t1 = threading.Thread(target=test2.send_post2)
    print(t1, star_time, test2.send_post2().json())
    t2 = threading.Thread(target=test2.send_post2)
    print(t2, star_time, test2.send_post2().json())
    t3 = threading.Thread(target=test2.send_post2)
    print(t3, star_time, test2.send_post2().json())
    t_list.append(t1)
    t_list.append(t2)
    t_list.append(t3)
    t1.start()
    t2.start()
    t3.start()
for t in t_list:
    t.join()

# 获取请求的平均响应时间
# post1_avg = sum(post1_times)/len(post1_times)
post2_avg = sum(post2_times)/len(post2_times)
# avg = {"登录平均响应时间": post1_avg, "提币平均响应时间": post2_avg}
avg = {"提币平均响应时间": post2_avg}
print(avg)




