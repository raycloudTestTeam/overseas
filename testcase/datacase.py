# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 17:12
#@File : datacase.py
#@remark :

import unittest
from driver import *
from login import *
from time import sleep
from  page.compage import *
from page.data1 import *

url="https://overseas.superseller.cn/index.html#/data/analysis/"
class DataTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # 如果所有的testcase 只运行一次那么要与class平级加上setUpModule
        cls.driver = Driver(url).start()
        cls.driver.maximize_window()
        Login(cls.driver).cookie_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #测试主流程校验
    def test_data_flowchart(self):
        result = []
        self.driver.get(url)
        sleep(1)
        menu_1 = ComPage(self.driver).left_menu(u"行业分析")
        result.append(menu_1)
        tab_1 = DataPage(self.driver).tab_click(u"行业概况")
        result.append(tab_1)
        tab_2 = DataPage(self.driver).tab_click(u"子行业概况")
        result.append(tab_2)
        tab_3 = DataPage(self.driver).tab_click(u"明星店铺")
        result.append(tab_3)
        tab_4 = DataPage(self.driver).tab_click(u"明星产品")
        result.append(tab_4)
        tab_5 = DataPage(self.driver).tab_click(u"飙升产品")
        result.append(tab_5)
        ding_talk(str(result),0)

def case_suite(*args):
    suite = unittest.TestSuite(map(DataTestCase,args))
    unittest.TextTestRunner().run(suite)


if __name__ =="__main__":
    unittest.main(verbosity=2)
