# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 10:32
#@File : orderbasepage.py
#@remark : 订单模块通用操作
from page.BasePage import *
class OrderAction(Action):

    # 搜索输入框 搜索
    def search(self,content):
        try:
            mixted = self.find_elem(
                    self.driver.find_element_by_name("mixedCondition2"))
            mixted.send_keys(content)
            mixted.send_keys(Keys.ENTER)

        except:
            print(u"搜索失败")
            log(u"%s :搜索内容失败" % content)
    # 清除筛选项
    def clear_filter(self):
        try:
            filter = self.find_elem(
                    self.driver.find_element_by_class_name("clear-all-filter"))
            filter.click()
        except:
            print(u"清除筛选项失败")
            log(u"清除筛选项失败")
    # 同步订单
    def syn_all(self):
        try:
            syn_btn = self.find_elem(
                    self.driver.find_element_by_css_selector("button[class~='btn-syn-all']"))
            syn_btn.click()
        except:
            print(u"同步订单报错")
            log(u"同步订单报错")

    # 指派相关人员操作点击
    def assign_user(self,name):
        try:
            log(u"订单指派开始")
            to_user = self.find_elem(
                    self.driver.find_element_by_css_selector("button[class~='assignUser']"))
            to_user.click()
            user_list = self.find_elem(
                    self.driver.find_element_by_css_selector("ul[class~='assign-list']"))

            user_list.find_element_by_link_text(name).click()
            self.assign_user_sure()
            self.alert_msg()
            log(u"订单指派结束")
        except:
            print(u"订单指派按钮")
            log(u"订单指派给%s 失败" % name)
    # 指派确认框点击
    def assign_user_sure(self,btn="ok"):
        dialog = self.find_elem(
                self.driver.find_element_by_class_name("ui_dialog"))
        content = dialog.find_element_by_class_name("ui_content")
        print(content)
        log(content)
        dialog.find_element_by_class_name("ui_state_highlight").click()

