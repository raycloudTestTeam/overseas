# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/15 10:11
#@File : ShopeeDataPage.py
#@remark : 虾皮数据page 对象
from  page.AllDataPage import DataAction
from data_driven.txthandle import *
class ShopeeData(DataAction):

    # 店铺列表关注操作
    def shop_table_focus(self):
        try:
            self.ids = TxtHandle().read_txt("shop_ids")[0]
            self.context_input(str(self.ids))
            self.search_click()
            if u"关注成功" in self.focus_success():
                print(u"----店铺列表关注成功------")

        except:
            print(u"店铺：%s  关注操作失败" % str(self.ids))

    # 产品列表关注
    def product_table_focus(self):
        pass


