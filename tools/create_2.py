# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/30 10:25
#@File : creat_order.py
#@remark : 新建手工订单

import unittest

from login import *
from driver import *
from selenium.webdriver.common.action_chains import ActionChains

class NewOrder2(unittest.TestCase):

    def setUp(self):
        url = "https://overseas.superseller.cn/index.html#/trade/list/?status=BUYER_PAY_END"
        self.driver = Driver(url,"Chrome").start()
        Login(self.driver).login()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_order_create(self):
        for i in range(100,150):
            self.driver.refresh()
            sleep(2)
            buttons = self.driver.find_element_by_css_selector("div.f-lt.trade-operation")
            btns = buttons.find_elements_by_class_name("btn-group")
            new = btns[-1]
            new.click()
            sleep(0.5)
            self.driver.find_element_by_class_name("J_new-order").click()
            sleep(0.5)
            value = "order-"+str(i)
            sku_name = "order-"+str(i)+"-"+str(i)
            phone = "12345678909"
            mail = "order-"+str(i)+"@"+str(i)+".com"
            self.driver.find_element_by_name("buyerId").send_keys(value)
            self.driver.find_element_by_name("buyerNick").send_keys(value)
            self.driver.find_element_by_name("receiverName").send_keys(value)
            self.driver.find_element_by_name("receiverCompany").send_keys(value)
            self.driver.find_element_by_name("phone").send_keys(phone)
            self.driver.find_element_by_name("state").send_keys(value)
            self.driver.find_element_by_name("city").send_keys(value)
            self.driver.find_element_by_name("streetAddress1").send_keys(value)
            self.driver.find_element_by_name("zipCode").send_keys("123212")
            self.driver.find_element_by_name("buyerEmail").send_keys(mail)
            self.driver.find_element_by_name("totalPrice").send_keys("1")
            self.driver.find_element_by_name("logisticsAmount").send_keys("1")
            self.driver.find_element_by_name("breakPrice").send_keys("1")
            self.driver.find_element_by_name("taxes").send_keys("1")
            sleep(0.5)
            na = self.driver.find_element_by_class_name("pd_20")
            na.find_element_by_tag_name("span").click()
            sleep(1)
            self.driver.find_element_by_name("sku").send_keys(sku_name)
            self.driver.find_element_by_name("title").send_keys(sku_name)
            self.driver.find_element_by_name("price").send_keys(str(1))
            self.driver.find_element_by_name("quantity").send_keys(str(1))
            sleep(1)
            b = self.driver.find_element_by_class_name("dialog_bottom")

            b.find_elements_by_tag_name("span")[1].click()
            sleep(1)
        sleep(2)
        items = self.driver.find_elements_by_xpath("//div[@data-tradetype='4']")
        for item in items:
            ActionChains(self.driver).double_click(item).perform()
            sleep(1)
            pd = self.driver.find_element_by_class_name("ui_content")
            box = pd.find_elements_by_class_name("ui-box")[3]
            box.find_element_by_tag_name("a").click()
            box.find_elements_by_tag_name("a")[2].click()
            box.find_element_by_name("sku").send_keys("order-33")
            box.find_element_by_name("chineseName").send_keys("order-33")
            box.find_element_by_name("englishName").send_keys("order-33")
            box.find_element_by_name("amount").send_keys("1")
            box.find_element_by_name("quantity").send_keys("1")
            box.find_element_by_name("weight").send_keys("1")
            box.find_elements_by_xpath("//span[@data-action='save']")[3].click()
            # box.find_element_by_partial_link_text(u"保存").click()

            sleep(3)
            self.driver.find_element_by_class_name("ui_close").click()
            sleep(2)

if __name__ =="__main__":
    unittest.main(verbosity=2)