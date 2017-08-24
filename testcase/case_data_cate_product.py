# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 15:47
#@File : case_data_cate_product.py
#@remark : 虾皮数据模块采集后-产品模块-上架发布

import unittest
from driver import *
from login import *
from page.data.s_itemme_page import *
from  page.data.s_itemdetailpage import *
class Case_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(url="https://overseas.superseller.cn/index.html#/data/").start()
        # cls.driver.get("https://overseas.superseller.cn/index.html#/data/")
        Login(cls.driver).login()
        cls.driver.maximize_window()
        cls.item_id = DataAction(cls).get_id("good")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def testcase_1(self):

        # 产品检索并采集
        url = "https://overseas.superseller.cn/index.html#/data_shopee/search_item/"
        SItemPage(self.driver).open_tab(url)
        item_search = SItemPage(self.driver)
        # item_id = item_search.get_id("good")
        item_search.search(self.item_id)
        item_search.collect()

        # 关注的产品列表点击名称进入详情页
        url = "https://overseas.superseller.cn/index.html#/data_shopee/item_me/"
        SItemMePage(self.driver).open_tab(url)
        item_me = SItemMePage(self.driver)
        item_me.search(self.item_id)
        item_me.to_detail()
        sleep(1)
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(1)

        # 详情页点击进入产品模块
        item_detail = SItemDetailPage(self.driver)
        item_detail.button_check(u"前往产品查看")
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])

        # 产品模块
        # print(self.driver.title)

if __name__ =="__main__":
    unittest.main(verbosity=2)












