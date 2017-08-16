# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 11:11
#@File : url_status.py
#@remark : 跨境url返回状态校验

import unittest
from driver import *
from login import *
import requests
import re
from  time import sleep
import os

class URL_Status(unittest.TestCase):

    def setUp(self):
        self.dr = Driver(url="",browser="HtmlUnit").start()
        self.dr.get("http://overseas.superseller.cn/index.html#/index/work/")
        sleep(0.5)
        self.dr.maximize_window()
        Login(self.dr).login()
        sleep(2)


    # 页面状态码(不是接口返回状态码)
    def test_all_url_statues(self):
        url_start = "http://overseas.superseller.cn/index.html#/"
        open_urls = ["index/work/","data/","data_shopee/",
                     "inventory/category/?status=INVENTORY","trade/list/?status=BUYER_PAY_END",
                     "package/","kefu/"]
        for open_url in open_urls:
            url = url_start+open_url
            self.dr.get(url)
            sleep(2)
            print(self.dr.title+"------start")
            page_source = self.dr.page_source
            link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", page_source,re.I|re.S|re.M)
            for link in link_list:
                if "http"in link:
                    try:
                        status = requests.get(link).status_code
                        if status !=200:
                            print(u'%s 打开状态为:%s'%(link,str(status)))
                    except:
                        print(u"打开失败")
                elif link == "":
                    pass
                elif "script" in link:
                    pass
                else:
                    link = "http://overseas.superseller.cn"+link
                    try:
                        status = requests.get(link).status_code
                        if status !=200:
                            print(u'%s 打开状态为:%s'%(link,str(status)))
                    except:
                        print(u"打开失败")
            print(self.dr.title+"------end")

    def tearDown(self):
        self.dr.quit()

if __name__ =="__main__":
    unittest.main(verbosity=2)


