# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:44
#@File : login.py
#@remark : 登录

from page.BasePage import Action
from selenium.webdriver.common.by import  By
value = ""

class Login(Action):

    @staticmethod
    def __user():
        return [u"",u""]

    # 这个不行，每次都要获取最新的cookies
    def cookie_login(self,login_cookie=""):
        # print(str(self))
        self.driver.delete_all_cookies()
        if login_cookie =="":
            self.driver.add_cookie({'name':'super_memSessionId1025',
                            'value':value})
        else:
            self.driver.add_cookie(login_cookie)

    def login(self):
        iframe = self.find_element(By.TAG_NAME,"iframe")
        self.switch_frame(iframe)
        self.driver.find_element(By.NAME, "userName").send_keys(self.__user()[0])
        self.driver.find_element(By.NAME, "pwd").send_keys(self.__user()[1])
        btn = self.driver.find_element(By.CSS_SELECTOR, "#loginPanel > div.btn.primary-btn.J_login")
        btn.click()




