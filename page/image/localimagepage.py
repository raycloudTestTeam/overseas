# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 11:11
#@File : localimagepage.py
#@remark : 本地图片管理

from page.image.imagebasepage import *

class LocalImagePage(ImageAction):

    # 搜索
    def search(self,content="",ty=1):
        nth = self.find_elem(self.driver.find_element_by_id("main-wrap"))
        local = nth.find_element_by_css_selector("div:nth-child(1)")
        if ty==1:
            search_input = local.find_element_by_name("J_image-search")
            search_input.send_keys(content+Keys.ENTER)
            sleep(1)

        else:
            search_type = local.find_element_by_class_name("J_search-type")
            search_type.click()
            search_type.find_element_by_css_selector("[value='2']").click()
            search_input = local.find_element_by_name("J_image-search")
            search_input.send_keys(content+Keys.ENTER)
            sleep(1)

    def nth_test(self):
        nth = self.driver.find_element_by_id("main-wrap")
        local = nth.find_element_by_css_selector("div:nth-child(1)")
        local.find_element_by_name("J_image-search").send_keys("222")
        sleep(10)

    #左侧菜单操作点击
    def left_menu_click(self,menu_name):
        try:
            left = self.find_elem(
                    self.driver.find_element_by_css_selector("[class~='new-subsub-li' and data-name='"+menu_name+"']"))
            left.click()
            log(u"%s 进入成功" %menu_name)
        except:
            log(u"%s 进入失败" %menu_name)

    # 新建分组操作
    def add_group(self,group_name):
        try:
            # group_name = "test"+str(random.randint(0,100))
            add_btn = self.find_elem(self.driver.find_element_by_css_selector("span[class~='J_add_group']"))
            add_btn.click()
            add_input = self.find_elem(self.driver.find_element_by_class_name("groupName"))
            add_input.send_keys(group_name)
            self.find_elem(self.driver.find_element_by_css_selector("span[class~='J_save']")).click()
            self.alert_msg()

        except:
            log(u"新建图片分组失败")