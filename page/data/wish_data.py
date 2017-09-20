# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/19 16:58
#@File : wish_data.py
#@remark : wish数据模块通用
from page.BasePage import *
class WishDataAction(Action):

    search_tabs ={"产品":"product","店铺":"shop","标签":"tag","行业":"industry"}

    # 页面点击动态加载-数据所有元素定位需要调用这个先
    def col_main(self):
        cols = self.driver.find_elements_by_class_name("wish_data-col-main")
        for col in cols:
            if col.is_displayed():
                return col
    # 导航条部分 -start
    # 导航条元素
    def bread(self):
        col_main = self.col_main()
        bread  =col_main.find_element_by_class_name("breadcrumb")
        return bread

    #获取导航条内容
    def bread_value(self):
        bread = self.bread()
        value = bread.find_element_by_class_name("pull-left").text
        print(value)
        log(value)

    #刷新当前页面
    def refresh(self):
        bread  = self.bread()
        bread.find_element_by_class_name("J_refresh").click()

    # 导航条数据定制点击
    def wish_custom_click(self):
        bread = self.bread()
        bread.find_element_by_class_name("icon-wish-data-custom-link").click()

    # 导航条部分 -end
    # 搜索内容部分 -start
    #  查询tab切换
    def search_change(self,name):
        ty = self.col_main().find_element_by_css_selector("[data-type='"+self.search_tabs[name]+"']")
        ty.click()
        sleep(1)

    # 查询内容输入
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
    # 搜索内容部分 -end


