# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/14 17:19
#@File : BasePage.py
#@remark : 封装所有页面都共用的方法
from selenium import webdriver
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from data_driven.txthandle import *
import sys

# 暂时不考虑亚马逊
top_menu_list ={"工作台":"index_nav","数据":"data_nav","产品":"inventory_nav","上架":"product_nav",
                "订单":"trade_nav","包裹":"package_nav","客服":"kefu_nav","图片":"image_nav"}

class Action(object):

    # 初始化
    def __init__(self,driver):
        self.driver = driver

    #打开页面，校验页面链接是否加载正确
    '''def _open(self,url,title):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(title),u"打开页面失败 %s" %url'''

    # 重写元素定位方法 再次封装
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            return  self.driver.find_element(*loc)
        except:

            print(u"%s 页面未找到 %s 元素,弹出框报错:%s" %(self,loc,str(self.alert_msg())))

    # 重写 switch_frame
    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)

    # 定义script 方法，执行js脚本，范围执行结果
    def script(self,js):
        self.driver.execute_script(js)


    # 定义菜单栏点击
    def menu_click(self,**kwargs):
        try:
            if kwargs['type'] == "top":
                top_nav = self.find_element(By.CLASS_NAME,"site-nav")
                top_nav.find_element(By.CLASS_NAME,top_menu_list[kwargs["name"]]).click()
            else:
                left_nav = self.find_element(By.CLASS_NAME, "new-left-ul")
                me = left_nav.find_element(By.XPATH, "//a[contains(text(),'"+kwargs["name"]+"')]")
                me.click()
        except:
            print(u"%s 的 %s 点击报错，检查菜单是否存在--- %s" % (kwargs["type"],kwargs["name"],self.alert_msg()))
            print(str(sys.exc_info()))


    # 报错弹出框内容获取
    def alert_msg(self):
        try:
            alert = self.find_element(By.CLASS_NAME("ui_content"),"ft_20")
            msg = alert.text
            return msg
        except:
            print(u"未找到弹出框")
            return ""

    # 列表翻页 , 1：第一页 2：往前一页 3：往后一页 4：最后一页
    def go_page(self,type):
        try:
            erp_pages = self.find_element(By.CLASS_NAME,"erp-pages")

            if type == 1:
                erp_pages.find_element("first-page").click()
            elif type == 2:
                erp_pages.find_element("prev-page").click()
            elif type == 3:
                erp_pages.find_element("next-page").click()
            else:
                erp_pages.find_element("last-page").click()
        except:
            return "%s 操作 翻页失败 --- %s" %(type,self.alert_msg())

