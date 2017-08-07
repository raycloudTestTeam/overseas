# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 17:02
#@File : compage.py
#@remark : 页面通用操作
import sys
from dingtalk import *
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ComPage(object):

    def __init__(self,driver):
        self.driver = driver

    # 左侧菜单通用点击 -start
    def left_menu(self,menu_name):
        try:
            left_ul = self.driver.find_element_by_class_name("new-left-ul")
            menu = left_ul.find_element_by_xpath("//a[contains(text(),'"+menu_name+"')]")
            # print(str(menu.text)+"-元素获取成功"+"/n")
            menu.click()
            print(str(menu.text))
            return u"True:进入"+menu_name+"页面成功"
        except:
            text = self.get_alert_value()
            return u"False: 进入"+menu_name+"页面失败，"+str(text)
    # 左侧菜单通用点击 -end

    #顶部菜单通用点击 -start
    def top_menu(self,menu_name):
        site_nav = self.driver.find_element_by_class_name("site-nav")
        nav = site_nav.find_element_by_xpath("//a[contains(text(),'"+menu_name+"')]")
        # nav = site_nav.find_element_by_css_selector("a[href='#/data/']")
        nav.click()
        sleep(1)
    #顶部菜单通用点击 -end

    # 顶部右侧模块设置点击 -start
    def site_setting(self,type=1,menu_name=""):
        result={}
        setting = self.driver.find_element_by_class_name("site-setting")
        drop = setting.find_element_by_css_selector("a[data-toggle=['dropdown']")
        drop.click()
        setting_menu = self.driver.find_element_by_css_selector("div.dropdown-menu.setting-dropdown-menu")

        # 2 点击相应的菜单 /1 返回用户名跟版本
        if type == 2:
            menu = setting_menu.find_element_by_xpath("//a[contains(text(),'"+menu_name+"')]")
            menu.click()
        else:
            name = setting_menu.find_element_by_class_name("uname")
            version = setting_menu.find_element_by_class_name("new-header-version")
            result[name] = version
            return result
    # 顶部右侧模块设置点击 -end

    # 通用showFail弹出框（div自定义弹出框） -satrt
    def get_alert_value(self):
        try:
            alert = self.driver.find_element_by_class_name("ui_content")
            text = alert.find_element_by_class_name("ft_20").text
            return text
        except:
            return ""


    # 最小化/最大化/还原/关闭(esc键)
    def show_button_click(self,button):
        buttons = self.driver.find_element_by_class_name("ui_title_buttons")
        buttons.find_element_by_css_selector("a[title='"+button+"']").click()

# 通用showFail弹出框（div自定义弹出框） -end


# 通用等待某个元素  -start
    def wait_element(self,element):
        wait = WebDriverWait(self.driver,10,0.5).until(EC.visibility_of(element),False)
        return wait

# 通用等待某个元素  -end


# 翻页控件通用操作 -start
    def pages(self):
        erp_pages = self.driver.find_element_by_class_name("erp-pages")
        return erp_pages

    #1到第一页，2往前一页，3往后一页，4最后一页
    def to_page(self,number):
        try:

            if number == 1:
                to_p = self.pages().find_element_by_class_name("first-page")
                to_p.click()
            elif number == 2:
                to_p = self.pages().find_element_by_class_name("prev-page")
                to_p.click()
            elif number == 3:
                to_p = self.pages().find_element_by_class_name("next-page")
                to_p.click()
            elif number == 4:
                to_p = self.pages().find_element_by_class_name("last-page")
                to_p.click()
            else:
                print(u"参数不对")
                return "True:翻页成功"
        except:
            text = self.get_alert_value()
            return "False: 翻页失败，"+text
    # 获取总页数
    def get_all_page(self):
        all_page = self.pages().find_element_by_class_name("last-page")
        return int(str(all_page.get_attribute("data-pages")))

# 翻页控件通用操作 -end

# 错误报错抛出
    def errorMsg(self,content):
        error = sys.exc_info()
        result = content +"-------"+str(error)
        # print(result)
        ding_talk(result,0)
        return result