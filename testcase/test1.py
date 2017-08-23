# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/18 9:53
#@File : test1.py
#@remark : tet

from driver import *
from selenium import webdriver
from page.BasePage import *

# dr = Driver("http://www.baidu.com").start()
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
dr.find_element_by_name("wd").send_keys("python")
print("1111")
