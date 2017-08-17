# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/17 11:57
#@File : all_coin.py
#@remark : 抓取所有单位

import unittest
from driver import *
from time import sleep
from dingtalk import *
from page.BasePage import *

class ALLCOIN(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(url="",browser="HtmlUnit").start()
        self.driver.get("http://erp103.tongtool.com/myaccount/exchangerate/index.htm")
        self.driver.maximize_window()
        name = self.driver.find_element_by_name("username")
        name.send_keys("362116814@qq.com")
        password = self.driver.find_element_by_name("password")
        password.send_keys("123456")
        self.driver.find_element_by_class_name("l_btn").click()
        sleep(3)

    def get_coin(self,coins):

        div = self.driver.find_element(By.ID,"showExchangeRate")
        table = div.find_elements_by_tag_name("table")[1]
        trs = table.find_elements_by_tag_name("tr")
        for index in range(1, len(trs)):
            tds = trs[index].find_elements_by_tag_name("td")
            key = tds[1].text
            value  = tds[2].text
            coins[key]=value
        return coins

    def test_get_all_coin(self):
        try:
            coins = {}
            re = self.get_coin(coins)
            page = self.driver.find_element_by_class_name("page")
            page.find_elements_by_tag_name("a")[1].click()
            sleep(2)
            re_1 = self.get_coin(re)
            ding_talk(str(re_1),0)
            print(str("OK"))
        except:
            print(str(sys.exc_info()))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)