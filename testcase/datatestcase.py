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
        re = shop_search.search(shop_id)
        if re =="success":
            shop_search.focus()

        # 取消关注店铺
        url = "https://overseas.superseller.cn/index.html#/data_shopee/shop_me/"
        SShopMePage(self.driver).open_tab(url)
        shop_me = SShopMePage(self.driver)
        shop_re = shop_me.search(shop_id)
        if shop_re =="success":
            shop_me.no_focus()

        # 产品检索
        url = "https://overseas.superseller.cn/index.html#/data_shopee/search_item/"
        SItemPage(self.driver).open_tab(url)
        item_search = SItemPage(self.driver)
        item_re = item_search.search(item_id)
        if item_re == "success":
            # item_search.focus()
            # SItemPage(self.driver).find_ele(By.NAME,"allId").click()
            # 产品采集
            item_search.collect()

        #取消关注产品
        url = "https://overseas.superseller.cn/index.html#/data_shopee/item_me/"
        SItemMePage(self.driver).open_tab(url)
        item_me = SItemMePage(self.driver)
        me_re = item_me.search(item_id)
        if me_re == "success":
            # item_me.collect()
            # SItemMePage(self.driver).find_ele(By.NAME,"teamAllId").click()
            #self.driver.find_element_by_name("teamAllId").click()
            item_me.no_focus()
        sleep(2)
        log(u"店铺："+shop_id+u"|产品："+item_id+u"---虾皮数据流程结束")

if __name__ =="__main__":
    unittest.main(verbosity=2)