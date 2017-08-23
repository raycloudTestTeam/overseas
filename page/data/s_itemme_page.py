# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 16:12
#@File : s_itemme_page.py
#@remark : 关注的产品页面
from page.data.databasepage import *
from page.data.s_item_page import *

class SItemMePage(DataAction):

    # 检索
    def search(self,content):
        try:
            self.data_search(content)
            self.data_search_click()
            if len(self.table_td())>=1:
                logging.info(u"关注的产品检索成功")
                sleep(1)
                return "success"
            else:
                logging.info(u"关注的产品未检索到该id-确认是否关注/采集成功")
                return "failed"
        except:
            logging.info("关注的产品检索失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    # 取消关注
    def no_focus(self):
        try:
            self.check_all()
            self.focus_items(u"取消关注")
            re = self.alert_msg()
            if u"成功" in re:
                logging.info(u"产品取消关注成功")
                return "success"
            else:
                logging.info(u"产品取消关注失败")
                return "failed"
        except:
            logging.info("产品取消关注失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    # 采集
    def collect(self):
        SItemPage(self.driver).collect()
