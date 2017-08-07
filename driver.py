# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:39
#@File : driver.py
#@remark : 浏览器驱动启动

from selenium import webdriver
import sys

class Driver():

    def __init__(self,url="",browser=""):
        self.url = url
        self.browser = browser

    def start(self):
        try:

            if self.browser == "Firefox":
                driver = webdriver.Firefox()
                driver.get(self.url)
                return driver

            elif self.browser == "IE":
                driver = webdriver.Ie()
                driver.get(self.url)

                return driver
            elif self.browser == "HtmlUnit":
                # 需要先启用 selenium-server
                driver = webdriver.Remote(self.url,desired_capabilities=webdriver.DesiredCapabilities.HTMLUNITWITHJS)
                return driver
            else: # 谷歌
                driver = webdriver.Chrome()
                driver.get(self.url)
                return driver

        except:

            print(str(sys.exc_info()))