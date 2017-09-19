# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/19 15:41
#@File : iamge_test_case.py
#@remark : 图片模块测试用例
import unittest
from driver import *
from login import *
from page.image.localimagepage import *
class ImageTestCase(unittest.TestCase):

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
        localimage = LocalImagePage(self.driver)
        localimage.top_menu("图片")
        # localimage.nth_test()
        localimage.search(content="11")
        localimage.search(ty=2)
        print("OK")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main(verbosity=2)
