# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/14 19:15
#@File : testcom.py
#@remark :

import  unittest
from driver import *
from login import *
from page.BasePage import *
from page.order.waitsendpage import *
class ComTest(unittest.TestCase):

    def setUp(self):
        self.dr = Driver(url="https://overseas.superseller.cn/index.html#/trade/list/?status=BUYER_PAY_END",
                         browser= "Chrome").start()
        self.dr.maximize_window()
        Login(self.dr).login()



    def test1(self):
        # Action(self.dr).menu_click(name=u"订单", type="top")
        #Action(self.dr).menu_click(name=u"衣服", type="left")
        sleep(1)
        f = self.dr.find_element_by_class_name("fixed-toolbar")
        f.find_element_by_css_selector("button.btn.btn-success.btn-syn-all").click()
        # WaitSendPage(self.dr).order_down()
        print(2)


    def tearDown(self):
        self.dr.quit()


if __name__ =="__main__":
    unittest.main(verbosity=2)