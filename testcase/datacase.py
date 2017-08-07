# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 17:12
#@File : datacase.py
#@remark :

import unittest
from driver import *
from login import *
url="https://overseas.superseller.cn/index.html#/data/analysis/"
class DataTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # 如果所有的testcase 只运行一次那么要与class平级加上setUpModule
        cls.driver = Driver(url,"HtmlUnit").start()
        cls.driver.maximize_window()
        Login(cls.driver).cookie_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_one(self):
        pass