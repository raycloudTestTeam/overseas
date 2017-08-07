# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:44
#@File : login.py
#@remark : 登录

class Login():

    def __init__(self,driver):
        self.dr = driver

    def cookie_login(self,login_cookie=""):
        # print(str(self))
        self.dr.delete_all_cookies()
        if login_cookie =="":
            self.dr.add_cookie({'name':'super_memSessionId1025',
                            'value':'aa90d92b3ea49c285f43b9bba9c835b90ab7d0f54a6b13b1d77d1fdffdf9709bff56a327f8239a022236ba9a6fcc103f'})
        else:
            self.dr.add_cookie(login_cookie)