# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 15:29
#@File : s_item_page.py
#@remark : 产品检索页面
from page.data.databasepage import *
import logging
from time import sleep
class SItemPage(DataAction):

    # 产品检索并检验
    def search(self,content):
        try:
            self.data_search(content)
            self.data_search_click()
            sleep(1)
            if len(DataAction(self.driver).table_tr())>=1:
                log(u"产品检索---查询id成功")
            else:
                log(u"产品检索--未检索到该产品id")

        except:
            log("产品检索--失败报错:%s" % DataAction(self.driver).alert_msg())
            print(str(sys.exc_info()))

    # 产品关注
    def focus(self):
        try:
            self.find_ele(By.NAME,"allId").click()
            self.focus_items(u"关注")
            re = self.alert_msg()
            log("产品检索："+re)
            '''if u"成功" in re:
                # log(u"产品检索-关注成功")
                return "success"
            else:
                log(u"产品检索-关注失败")
                return "failed"'''
        except:
            log("产品检索--关注失败报错:%s|%s" %(self.alert_msg()))

    # 产品采集
    def collect(self):

        try:
            self.find_ele(By.NAME,"allId").click()
            self.focus_items(u"采集")
            coll = self.collect_win()
            if u"已采集" in coll:
                log(u"该产品已经被采集过")
                self.find_ele(By.NAME,"allId").click()
            else:
                self.collect_win_ok()
                self.collecting()

        except:
            log("产品检索--采集报错:%s" %(self.alert_msg()))
            print(str(sys.exc_info()))
