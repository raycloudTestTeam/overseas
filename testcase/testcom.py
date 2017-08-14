# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/14 19:15
#@File : testcom.py
#@remark :

import  unittest
from driver import *
from login import *
from page.BasePage import *
class ComTest(unittest.TestCase):

    def setUp(self):
        self.dr = Driver(url="https://overseas.superseller.cn/index.html#/data/analysis/").start()
        self.dr.maximize_window()
        Login(self.dr).login()



    def test1(self):
        Action(self.dr).menu_click(name=u"产品", type="top")
        Action(self.dr).menu_click(name=u"衣服", type="left")
        print(1)

    def tearDown(self):
        self.dr.quit()


if __name__ =="__main__":
    unittest.main(verbosity=2)