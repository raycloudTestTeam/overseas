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
            if len(self.table_td())>=1:
                logging.info(u"产品检索成功")
                sleep(1)
                return "success"
            else:
                logging.info(u"未检索到该产品id")
                return "failed"

        except:
            logging.info("产品检索失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    # 产品关注
    def focus(self):
        try:
            self.find_ele(By.NAME,"allId").click()
            self.focus_items(u"关注")
            re = self.alert_msg()
            if u"成功" in re:
                logging.info(u"产品检索-关注成功")
                return "success"
            else:
                logging.info(u"产品检索-关注失败")
                return "failed"
        except:
            logging.info("产品检索关注失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    # 产品采集
    def collect(self):

        try:
            self.find_ele(By.NAME,"allId").click()
            self.focus_items(u"采集")
            coll = self.collect_win()
            if u"已采集" in coll:
                pass
            else:
                self.collect_win_ok()
                self.collecting()

        except:
            logging.info("产品检索关注失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))
