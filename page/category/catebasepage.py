# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 10:03
#@File : catebasepage.py
#@remark : 产品模块公用操作
from page.BasePage import *

class CateAction(Action):

    def search_input(self,content):
        self.find_ele(By.NAME,"keyword").send_keys(content)

    def search_click(self):
        self.find_ele(By.NAME,"keyword").send_keys(Keys.ENTER)

    def table_ele(self):
        body = self.find_ele(By.CLASS_NAME,"erp-table-tbody")
        data = body.find_elements_by_class_name("erp-image-hover-div")
        return data

