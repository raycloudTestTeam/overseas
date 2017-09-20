# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 14:19
#@File : s_shopme_page.py
#@remark : 虾皮数据-关注的店铺页面-作废
from page.data.databasepage import *

class SShopMePage(DataAction):

    def search(self,content):
        try:
            self.data_search(content)
            self.data_search_click()
            sleep(1)
            if len(self.table_tr())>=1:
                log(u"关注的店铺-检索id成功")
                # return "success"
            else:
                log(u"关注的店铺--未检索到该id")
                # return "failed"
        except:
            log("关注的店铺--检索失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    def no_focus(self):
        try:
            self.check_all()
            self.focus_items(u"取消关注")
            re = self.alert_msg()
            log(u"关注的店铺:"+re)
            '''if u"成功" in re:
                log(u"店铺取消关注成功")
                return "success"
            else:
                log(u"店铺取消关注失败")
                return "failed"'''
        except:
            log("店铺取消关注失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))
