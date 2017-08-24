# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 10:54
#@File : datatestcase.py
#@remark : 数据模块测试脚本
import unittest
from driver import *
from login import *
from page.data.s_shop_page import *
from data_driven.log import *
from page.data.s_shopme_page import *
from page.data.s_item_page import *
from page.data.s_itemme_page import *
class DataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(url="https://overseas.superseller.cn/index.html#/data/").start()
        # cls.driver.get("https://overseas.superseller.cn/index.html#/data/")
        Login(cls.driver).login()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 虾皮主流程
    def test_shopee_all(self):

        # 关注店铺
        url = "https://overseas.superseller.cn/index.html#/data_shopee/search_shop/"
        SShopPage(self.driver).open_tab(url)
        shop_search = SShopPage(self.driver)
        shop_id = shop_search.get_id("shop")
        item_id = shop_search.get_id("good")
        log(u"店铺："+shop_id+u"|产品："+item_id+u"---虾皮数据流程开始")
        shop_search.search(shop_id)
        shop_search.focus()

        # 取消关注店铺
        url = "https://overseas.superseller.cn/index.html#/data_shopee/shop_me/"
        SShopMePage(self.driver).open_tab(url)
        shop_me = SShopMePage(self.driver)
        shop_me.search(shop_id)
        shop_me.no_focus()

        # 产品检索
        url = "https://overseas.superseller.cn/index.html#/data_shopee/search_item/"
        SItemPage(self.driver).open_tab(url)
        item_search = SItemPage(self.driver)
        item_search.search(item_id)
        item_search.collect()

        #取消关注产品
        url = "https://overseas.superseller.cn/index.html#/data_shopee/item_me/"
        SItemMePage(self.driver).open_tab(url)
        item_me = SItemMePage(self.driver)
        item_me.search(item_id)
        item_me.no_focus()
        sleep(2)
        log(u"店铺："+shop_id+u"|产品："+item_id+u"---虾皮数据流程结束")

if __name__ =="__main__":
    unittest.main(verbosity=2)