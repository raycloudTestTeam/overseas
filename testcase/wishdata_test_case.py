# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/19 17:23
#@File : wishdata_test_case.py
#@remark : wish数据模块测试用

import unittest
from driver import *
from login import *
from page.data.wish_data_index import *
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
        print(u"wish数据开始")

    @classmethod
    def tearDownClass(cls):
        print(u"wish数据结束")
        cls.driver.quit()

    def test_index(self):
        print(u"wish数据-全站分析-start")
        dara_index = WishDataIndexPage(self.driver)
        dara_index.bread_value()
        dara_index.all_count(table_type='product')
        dara_index.amount7_table(table_type='product')
        dara_index.script("document.documentElement.scrollTop=1000")
        dara_index.all_count(table_type='shop')
        dara_index.amount7_table(table_type='shop')
        print(u"wish数据-全站分析-end")
        #wish_data.top_menu(u"数据")
        #wish_data.search(name="店铺", content="53b7bace46188e74de5f7e7d")
        #wish_data.bread_value()
        #wish_data.product_all_table()
        #wish_data.get_amount7_table()
        #wish_data.open_amount7_product("11~50")
        sleep(4)
        print("OK")

if __name__ =="__main__":
    unittest.main(verbosity=2)
