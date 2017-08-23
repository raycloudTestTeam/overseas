# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 10:14
#@File : 1.py
#@remark : 店铺检索页面（数据有个很尴尬的点，每点一个菜单加载内容，之前的内容不消失，会导致页面元素定位问题）

from page.data.databasepage import *
from data_driven.log import *
from time import sleep
class SShopPage(DataAction):

    # 店铺查询并校验
    def search(self,content):
        try:
            self.data_search(content)
            self.data_search_click()
            if len(self.table_td())>=1:
                log(u"检索成功")
                sleep(1)
                return "success"
            else:
                log(u"未检索到该id")
                return "failed"

        except:
            log("店铺检索失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))

    # 店铺关注并校验(暂时只支持全选，不支持自定义勾选)
    def focus(self):
        try:
            self.check_all()
            self.focus_items(u"关注")
            re = self.alert_msg()
            if u"成功" in re:
                log(u"店铺检索关注成功")
                return "success"
            else:
                log(u"店铺检索关注失败")
                return "failed"
        except:
            log("店铺检索关注失败报错:%s|%s" %(self.alert_msg(),str(sys.exc_info())))



if __name__ =="__main__":
    pass