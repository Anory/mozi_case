#/usr/bin/python
#encoding:utf-8
import _csv
import os
import time


# 启动类
class Cpu(object):
    def __init__(self):
        self.adbvalua = ""
        self.cpuvalua = 0

    # 启动ADB命令
    def adb(self):
        cmd = 'adb shell "dumpsys cpuinfo | grep com.mozi.smart"'
        self.adbvalua = os.popen(cmd)

    # 获取cpu使用率
    def cpu(self):
        for line in self.adbvalua.readlines():
            print("line:", line)
            self.cpuvalue = line.split("%")[0]
            break
        return self.cpuvalue

# 控制类
class Controller(object):
    def __init__(self, count):
        self.cpu = Cpu()
        self.counter = count
        self.data = [("timestamp", "cpustatus")]

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 单次测试过程
    def testProcess(self):
        self.cpu.adb()
        time.sleep(20)
        valua = self.cpu.cpu()
        print("cpu使用率：", valua)
        currenttime = self.getCurrentTime()
        print("当前时间：", currenttime)
        self.data.append((currenttime, valua))
        # print(self.data)

    # 多次执行测试方法
    def run(self):
        while self.counter > 0:
            self.testProcess()
            self.counter = self.counter - 1
            time.sleep(5)

    # 数据写入文件
    def SaveDataToCSV(self):
        csvfile = open('cpu.csv', 'w')
        writer = _csv.writer(csvfile)
        writer.writerows(self.data)
        csvfile.close()


if __name__ == "__main__":
    cmd = r'adb shell monkey -p com.mozi.smart --throttle 200 -v -v 5000 > E:\test.txt'
    os.popen(cmd)
    controller = Controller(20)
    controller.run()
    controller.SaveDataToCSV()

