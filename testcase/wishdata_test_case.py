# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/19 17:23
#@File : wishdata_test_case.py
#@remark : wish数据模块测试用

import unittest
from driver import *
from login import *
from page.data.wish_data import *
class WishDataTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(url="https://overseas.superseller.cn/index.html#/data/",
                            browser="Chrome").start()
        cls.driver.maximize_window()
        status = Login(cls.driver).login(t="on")
        if  status == "False":
            cls.tearDownClass()
        else:
            sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1(self):
        wish_data = WishDataAction(self.driver)
        wish_data.top_menu(u"数据")
        wish_data.search(name="店铺", content="53b7bace46188e74de5f7e7d")
        sleep(4)
        print("OK")

if __name__ =="__main__":
    unittest.main(verbosity=2)
