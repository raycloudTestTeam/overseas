# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:44
#@File : login.py
#@remark : 登录

from page.BasePage import Action
from selenium.webdriver.common.by import  By
from data_driven.txthandle import *
from time import sleep
from data_driven.log import *
value = ""

class Login(Action):

    @staticmethod
    def __user(t="test"):
        if t=="test":
            user = TxtHandle().read_txt("user")
        else:
            user = TxtHandle().read_txt("user_on")

        for u in user:
            U = u.split(',')
            return U

    # 这个不行，每次都要获取最新的cookies
    def cookie_login(self,login_cookie=""):
        # print(str(self))
        self.driver.delete_all_cookies()
        if login_cookie =="":
            self.driver.add_cookie({'name':'super_memSessionId1025',
                            'value':value})
        else:
            self.driver.add_cookie(login_cookie)

    def login(self,t="test"):
        try:
            iframe = self.find_elem(self.driver.find_element_by_css_selector("iframe[frameborder='0']"))
            self.switch_frame(iframe)
            user = self.__user(t)
            self.find_elem(self.driver.find_element_by_name("userName")).send_keys(user[0])
            self.find_elem(self.driver.find_element_by_name("pwd")).send_keys(user[1])
            login_button = self.driver.find_element_by_css_selector("[class~='J_login']")
            login_button.click()
            sleep(1)
            print("登录成功")
            log(str(self.__user())+u"登录成功")
            return "True"
        except:
            print("登录失败")
            log(str(self.__user())+u"登录失败")
            return "False"








