# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/15 10:12
#@File : AllDataPage.py
#@remark : 数据模块通用操作
from page.BasePage import *

# (目前只试用虾皮部分的所有搜索输入)
class DataAction(Action):

    # 搜索内容输入操作(目前只试用虾皮部分的所有搜索输入)
    def context_input(self,content):
        self.find_element(By.CLASS_NAME,"ipt-search-item").send_key(content)

    # 执行搜索
    def search_click(self):
        self.find_element(By.CLASS_NAME,"ipt-search-item").send_key(Keys.ENTER)

    # 保存筛选项
    def save_filter(self):
        pass

    # 删除筛选项
    def clear_filter(self):
       self.find_element(By.CLASS_NAME,"clear-all-filter").click()

    # 返回列表的tr元素
    def table_ele(self):
        table =  self.find_element(By.CLASS_NAME,"data-simple-table")
        trs = table.find_elements_by_class_name("tr-item")
        return trs

    # table数据全选
    def item_all(self):
        self.find_element(By.NAME,"allId").click()

    # 列表操作按钮列表点击
    def focus_collect_items(self,type):
        try:
            buttons = self.find_element(By.ID,"BUTTON-CONTAIENER")
            if type == u"关注":
                buttons.find_element(By.LINK_TEXT,u"关注").click()
            else:
                buttons.find_element(By.LINK_TEXT,u"采集").clik()
        except:

            print("%s 操作失败,弹出框报错：%s，实际报错：%s",(type,self.alert_msg(),str(sys.exc_info())))

    #采集弹出框确认操作
    def collect_OK(self):
        try:
            dia = self.find_element(By.CLASS_NAME,"dialog_bottom")
            dia.find_element(By.LINK_TEXT,u"确定")
        except:
            print("采集产品确认失败：%s",(str(sys.exc_info())))

    # 采集进度反馈
    def collect_schedule(self):
        print( str(self.find_element(By.CLASS_NAME,"process-context").text))
        return self.find_element(By.CLASS_NAME,"process-context").text

    # 关注成功反馈
    def focus_success(self):
        print(self.alert_msg())
        return (self.alert_msg())

