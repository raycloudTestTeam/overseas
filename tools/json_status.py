# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 18:08
#@File : json_status.py
#@remark : 线上的Json返回结果

import unittest
from driver import *
from login import *
import requests
import re
import json
from  time import sleep
from data_driven.xmlhandle import *
class Json_Status(unittest.TestCase):

    def setUp(self):
        self.user = {}
        self.dr = Driver(url="",browser="HtmlUnit").start()
        self.dr.get("http://overseas.superseller.cn/index.html#/index/work/")
        sleep(0.5)
        self.dr.maximize_window()
        Login(self.dr).login()
        sleep(1)
        all_cookies = self.dr.get_cookies()
        for cook in all_cookies:
            if cook["name"] == "super_memSessionId1025":
                self.user["super_memSessionId1025"] = cook["value"]
        sleep(2)



    def test_run(self):
        try:
            # xml = XmlHandle().open("online_api")
            json_list = XmlHandle().get_elements("online_api","json")
            for j in json_list:
                url = XmlHandle().get_item_value(j,"url") # json链接
                type_name = XmlHandle().get_item_value(j,"type") # 传递类型
                pare = XmlHandle().get_item_value(j,"pars") # 参数类型
                if type_name == "POST":
                    coll = requests.post(url,cookies=self.user)
                    code_status = coll.status_code
                    if code_status == 200:
                        status = coll.json()["result"]
                        print("%s 的返回状态为%s" %(url,status))
                    else:
                        print("%s 的返回状态为%s" %(url,coll))

                else:
                    coll = requests.get(url,cookies=self.user)
                    code_status = coll.status_code
                    if code_status == 200:
                        status = coll.json()["result"]
                        print("%s 的返回状态为%s" %(url,status))
                    else:
                        print("%s 的返回状态为%s" %(url,coll))
        except:
            print(str(sys.exc_info()))

    def tearDown(self):
        self.dr.quit()


if __name__ =="__main__":
    unittest.main(verbosity=2)

