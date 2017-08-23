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
from time import sleep
import logging

# 暂时不考虑亚马逊
top_menu_list ={"工作台":"index_nav","数据":"data_nav","产品":"inventory_nav","上架":"product_nav",
                "订单":"trade_nav","包裹":"package_nav","客服":"kefu_nav","图片":"image_nav"}

class Action(object):

    # 初始化
    def __init__(self,driver):
        self.driver = driver

    # 重写元素定位方法 再次封装
    def find_ele(self,*loc):
        try:
            WebDriverWait(self.driver,5,0.5).until(lambda driver:driver.find_element(*loc).is_displayed())
            return  self.driver.find_element(*loc)
        except:
            logging.info("元素：%s 未找到"%loc)
            pass


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
                top_nav = self.find_ele(By.CLASS_NAME,"site-nav")
                top_nav.find_ele(By.CLASS_NAME,top_menu_list[kwargs["name"]]).click()
            else:
                left_nav = self.find_ele(By.CLASS_NAME, "new-left-ul")
                me = left_nav.find_ele(By.XPATH, "//a[contains(text(),'"+kwargs["name"]+"')]")
                me.click()
        except:
            logging.error(u"%s 元素未找到，弹出框报错：%s" % (kwargs["name"],self.alert_msg()))


    # 报错弹出框内容获取
    def alert_msg(self):
        try:
            alert = self.find_ele(By.CLASS_NAME,"ui_content")
            re = alert.find_element_by_class_name("ft_20")
            msg = re.text
            sleep(1)
            return msg
        except:
            # print(u"未找到弹出框")
            return ""

    # 列表翻页 , 1：第一页 2：往前一页 3：往后一页 4：最后一页
    def go_page(self,type):
        try:
            erp_pages = self.find_ele(By.CLASS_NAME,"erp-pages")

            if type == 1:
                erp_pages.find_ele("first-page").click()
            elif type == 2:
                erp_pages.find_ele("prev-page").click()
            elif type == 3:
                erp_pages.find_ele("next-page").click()
            else:
                erp_pages.find_ele("last-page").click()
        except:
             logging.error(u"%s 操作 翻页失败 --- %s" %(type,self.alert_msg()))
             pass

