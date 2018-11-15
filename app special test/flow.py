import _csv
import os
import time


# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.receive = 0
        self.receive2 = 0
        self.transmit = 0
        self.transmit2 = 0
        self.data = [("timestamp", "traffic")]

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 单次测试过程
    def testProcess(self):
        # 执行获取进程的命令
        result = os.popen('adb shell "ps | grep com.mozi.smart"')
        # 将进程信息由list装换成str
        a = ("".join(result.readlines()))
        # 将字符串里面的pid提取出来
        pid = a.split(" ", 9)[4]
        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/"+pid+"/net/dev")
        for line in traffic:
            if "eth0" in line:
                # 将获取到的数据转换成str
                line = "#".join(line.split())
                # 按空格号拆分,获取收到和发出的流量
                self.receive = line.split(" ")[1]
                self.transmit = line.split(" ")[9]
            elif "eth1" in line:
                # 将获取出来的数据转换成str
                line = " ".join(line.split())
                # 按空格号拆分,获取收到和发出的流量
                self.receive2 = line.split(" ")[1]
                self.transmit2 = line.split(" ")[9]
        print("获取到的流量 :", self.transmit2, self.receive2, self.receive, self.transmit)
        # 计算所有流量的之和
        traffic = (int(self.receive) + int(self.transmit) + int(self.receive2) + int(self.transmit2))
        print("流量总和：", traffic)
        # 按KB计算流量值
        all_traffic = traffic/1024
        print("按KB计算后的流量总和：", all_traffic)
        # 获取当前时间
        current_time = self.getCurrentTime()
        # 将获取到的数据存到数组中
        self.data.append((current_time, all_traffic))

    # 多次测试过程控制
    def run(self):
        while self.counter > 0:
            self.testProcess()
            self.counter = self.counter - 1
            # 每10秒钟采集一次数据
            time.sleep(15)

    # 数据的存储
    def saveDataToCSV(self):
        csvfile = open('traffic.csv', 'w')
        writer = _csv.writer(csvfile)
        writer.writerows(self.data)
        csvfile.close()


if __name__ == "__main__":
    cmd = r'adb shell monkey -p com.mozi.smart --throttle 200 -v -v 5000 > E:\test.txt'
    os.popen(cmd)
    controller = Controller(20)
    controller.run()
    controller.saveDataToCSV()
