import unittest
from mozi.moziclass import RunMain
import time
import pymysql
from ddt import ddt, data, unpack
from mozi import HTMLTestRunner

# 链接开彩数据库
kaicai_connect = pymysql.Connect(
    host='192.168.1.222',
    port=3306,
    user='root',
    passwd='kaicai365',
    db='kaicai_new',
    charset='utf8'
)

# 链接墨子数据库
mozi_connect = pymysql.Connect(
    host='192.168.1.191',
    port=3306,
    user='root',
    passwd='Mz18!@#qwer',
    db='mozi',
    charset='utf8'
)

# 获取游标
kaicai_cursor = kaicai_connect.cursor()
mozi_cursor = mozi_connect.cursor()

@ddt
class RunTest(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        sql = "UPDATE opt_auth_code SET status = '%s' WHERE phone = '%s'"
        data = (0, '13265556550')
        kaicai_cursor.execute(sql % data)
        kaicai_connect.commit()
        print('成功修改', kaicai_cursor.rowcount, '条数据')

        sql = "UPDATE opt_auth_code SET status = '%s' WHERE phone = '%s'"
        data = (0, '13265556550')
        mozi_cursor.execute(sql % data)
        mozi_connect.commit()
        print('成功修改', mozi_cursor.rowcount, '条数据')

    # 登录
    @data((' ', 1000), (123456, 1000), ('哈哈哈哈', 1000), ('bnuagbbdbvubgugbk', 1000), ('0OzHpm36GBvMAdgl7JzrVQ==', 200))
    @unpack
    def test1Case(self, password, valua):
        url = 'http://api-robot.mozi.local/v1/user/login'
        data = {
            'account': 'jies',
            'password': password,
            'device_id': '1',
            'os_ver': '1'
        }
        headers = {
            'app-ver': '104'
        }
        res = self.run.run_main(url, 'POST', data, headers)
        print("登录返回信息：", res)
        self.assertEqual(res["code"], valua, "验证失败")
        time.sleep(3)

    # 修改密码
    @data(('', 1000), (123456, 1000), ('nabubjbvgubbggbb', 1000), ('哈啊教大家分别骄傲', 1000),
          ('@#$%^&@#$%^&', 1000), ('XSuXLc4YwD18416185wIB/37nwgFg==', 1000), ('0OzHpm36GBvMAdgl7JzrVQ==', 200))
    @unpack
    def test2Case(self, password, valua):
        url = 'http://api-robot.mozi.local/v1/user/resetpwd'
        data = {
            'mobile': '13265556550',
            'password': password,
            'code': '9483'
        }
        headers = {
            'app-ver': '104'
        }
        print(headers)
        res = self.run.run_main(url, 'POST', data, headers)
        print("header:", res)
        print("修改密码返回信息：", res)
        self.assertEqual(res['code'], valua, "验证失败")
        time.sleep(3)

    # 设置支付密码和验证问题
    @data((' ', ' ', 1000), ('哈哈哈哈', ' ', 1000), ('M77IRdWTz哈哈哈哈NieMe7pJ', '0OzHpm36GBvMAdgl7JzrVQ==', 1000),
          ('M77IRdWTzNieMe7pJ409yg===', '0OzHpm36GBvMAdgl7JzrVQ==', 200))
    @unpack
    def test3Case(self, answer, password, vulua):
        sql = "DELETE FROM `user_safety` WHERE user_id = '1525682336000540'"
        sql2 = "UPDATE `user_info` SET payment_password = '%s' WHERE id = '%s'"
        data = ('', '1525682336000540')
        mozi_cursor.execute(sql2 % data)
        mozi_cursor.execute(sql)
        mozi_connect.commit()
        print('成功修改', mozi_cursor.rowcount, '条数据')
        url = 'http://api-robot.mozi.local/v1/user/login'
        data = {
            'account': 'jies',
            'password': '123456',
            'device_id': '1',
            'os_ver': '1'
        }
        res = self.run.run_main(url, 'POST', data)
        token = (res["data"]["token"])
        time.sleep(3)
        # 设置支付密码
        url = 'http://api-robot.mozi.local/v1/user/set-payment-pwd'
        data = {
            'token': token,
            'v_code': '7812',
            'question_id': '1',
            'question_answer': answer,
            'trade_password': password
        }
        res = self.run.run_main(url, 'POST', data)
        print("设置支付密码返回信息：", res)
        self.assertEqual(res['code'], vulua, "验证失败")

    # 验证安全问题
    @data(('', 1000), ('哈哈哈哈', 1000), ('M77IRdWTzNieMe7pJ40', 1000), ('M77IRdWTzNieMe7pJ409yg===', 200))
    @unpack
    def test4Case(self, answer, valua):
        url = 'http://api-robot.mozi.local/v1/user/login'
        data = {
            'account': 'jies',
            'password': '123456',
            'device_id': '1',
            'os_ver': '1'
        }
        res = self.run.run_main(url, 'POST', data)
        token = (res["data"]["token"])
        time.sleep(3)
        url = 'http://api-robot.mozi.local/v1/user/verify-problem'
        data = {
            'token': token,
            'type': '1',
            'question_id': '1',
            'question_answer': answer,
            'v_code': '7812'
        }
        res = self.run.run_main(url, 'POST', data)
        print("验证安全问题返回信息：", res)
        self.assertEqual(res["code"], valua, "验证失败")
        time.sleep(3)


    # 重置交易密码
    @data(('', 1000), (123456, 1000), ('#￥%……&*（@#￥%……&*@#￥%……', 1000), ('0OzHpm36GBvMAdgl7JzrVQ==', 200))
    @unpack
    def test5Case(self, answer, valua):
        url = 'http://api-robot.mozi.local/v1/user/login'
        data = {
            'account': 'jies',
            'password': '123456',
            'device_id': '1',
            'os_ver': '1'
        }
        res = self.run.run_main(url, 'POST', data)
        token = (res["data"]["token"])
        self.assertEqual(res["code"], 200, "验证失败")
        time.sleep(3)

        # 修改验证码使用状态
        sql = "UPDATE opt_auth_code SET status = '%s' WHERE phone = '%s'"
        data = (0, '13265556550')
        mozi_cursor.execute(sql % data)
        mozi_connect.commit()
        print('成功修改', mozi_cursor.rowcount, '条数据')
        url = 'http://api-robot.mozi.local/v1/user/verify-problem'
        data = {
            'token': token,
            'type': '1',
            'question_id': '1',
            'question_answer': 'M77IRdWTzNieMe7pJ409yg===',
            'v_code': '7812'
        }
        res = self.run.run_main(url, 'POST', data)
        print("验证安全问题返回信息：", res)
        pass_code = (res["data"]["pass_code"])
        self.assertEqual(res["code"], 200, "验证失败")
        time.sleep(3)
        # 重置交易密码
        url = 'http://api-robot.mozi.local/v1/user/reset-payment-pwd'
        data = {
            'token': token,
            'trade_password': answer,
            'pass_code': pass_code
        }
        res = self.run.run_main(url, 'POST', data)
        print("重置密码返回信息：", res)
        self.assertEqual(res["code"], valua, "验证失败")
        time.sleep(3)

    # 修改钱包地址/设置钱包名称
    @data((1234567891234567891234567897896541236547896541259555565655555555, 1000), ('', 1000),
          ('37030736df3a6cf9fb21932a08bc2ceb5a7f9ceb9a2151cbb3001df4ea10e1c', 1000),
          ('37030736df3a6cf9fb21932a08bc2ceb5a7f9ceb9a2151cbb3001df4ea10e1cca', 1000),
          ('isinnnnnssdqeyuiokjtgsnjgtrmkaijnhfreihbgnfopiutredjgkofdlngcf', 1000),
          ('37030736df3a6cf9fb21932a08bc2ceb5a7f9ceb9a2151cbb3001df4ea10e1cs', 200))
    @unpack
    def test6Case(self, address, valua):
        url = 'http://api-robot.mozi.local/v1/user/login'
        data = {
            'account': 'jies',
            'password': '123456',
            'device_id': '1',
            'os_ver': '1'
        }
        res = self.run.run_main(url, 'POST', data)
        token = (res["data"]["token"])
        time.sleep(3)
        url = 'http://api-robot.mozi.local/v1/wallet/setting'
        data = {
            'token': token,
            'wallet_address': address,
            'wallet_name': '聚宝盘'
        }
        res = self.run.run_main(url, 'POST', data)
        print("修改钱包地址/名称返回信息：", res)
        self.assertEqual(res["code"], valua, "验证失败")
        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(RunTest("test1Case"))
    suite.addTest(RunTest("test2Case"))
    suite.addTest(RunTest("test3Case"))
    suite.addTest(RunTest("test4Case"))
    suite.addTest(RunTest("test4Case"))
    print("完成测试")
    filepath = "../report/htmlrepot.html"
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="墨子接口测试报告")
    runner.run(suite)
    fp.close()

