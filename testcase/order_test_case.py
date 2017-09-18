# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/18 15:47
#@File : order_test_case.py
#@remark : 订单测试用例

import unittest
from driver import *
from login import *
from page.order.orderbasepage import *
class OrderTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(url="https://overseas.superseller.cn/index.html#/trade/list/?status=WAIT_SELLER_SEND_GOODS",
                            browser="Chrome").start()
        cls.driver.maximize_window()
        status = Login(cls.driver).login()
        if  status == "False":
            cls.tearDownClass()

        else:
            sleep(2)


    def test_1(self):
        self.driver.find_element_by_name("allId").click()
        OrderAction(self.driver).assign_user("魔法小圆")
        print("OK")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main(verbosity=2)
