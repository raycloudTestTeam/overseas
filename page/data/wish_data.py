# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/19 16:58
#@File : wish_data.py
#@remark : wish数据模块通用
from page.BasePage import *
class WishDataAction(Action):
    # 搜索内容部分
    search_tabs ={"产品":"product","店铺":"shop","标签":"tag","行业":"industry"}

    def col_main(self):
        # 有问题 明天看
        col = self.driver.find_element_by_css_selector(".class_value:visible")
        return col
        # col_main.find_element_by_class_name("J_search-tab-input").send_keys("aaa")

    def search_change(self,name):
        ty = self.col_main().find_element_by_css_selector("[data-type='"+self.search_tabs[name]+"']")
        ty.click()
        sleep(1)

    def input_content(self,content):
        inputs = self.col_main().find_element_by_class_name("J_search-tab-input")
        inputs.send_keys(content+Keys.ENTER)
        sleep(1)
    # 切换tab搜索流程
    def search(self,name,content):
        try:
            self.search_change(name)
            self.input_content(content)
            log(u"%s 搜索 %s 成功" % (name,content))
        except:
            print(str(sys.exc_info()))
            log(u"%s 搜索 %s 失败" % (name,content))
