# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/18 13:54
#@File : 元素定位合集.py
#@remark : 各种元素定位使用方法
from selenium import webdriver
driver = webdriver.Chrome()

def id():
    # 注定部分动态加载id属性值
    driver.find_element_by_id("XX")

# xpath 非常实用
def xpath():
    driver.find_element_by_xpath("//input[@class='' and @name='']")  # 组合属性定位
    driver.find_element_by_xpath("//input[contains(@class,'s')]") # class属性包含s
    #基础定位
    driver.find_element_by_xpath("//标签名[@属性=‘属性值’]")

    # 通过元素内容定位
    driver.find_element_by_xpath("//p[contains(text(),'xxx')]")
    #标签指定下包含属性值组合定位
    driver.find_element_by_xpath("//p[contains(text(),'xx') and @id='xx']")

def class_name():
    # 根据class的属性值定位，但是不能适用于组合class的情况
    driver.find_element_by_class_name("XX")


def tag_name():
    # 根据标签名称定位，慎用，基本会出现查找到元素list的情况
    # 但是适用于复选框全部一起勾选
    driver.find_element_by_tag_name("xx")

def name():
    #通过name属性的值进行定位,也会出现重复名称的情况
    driver.find_element_by_name("XX")

def link_text():
    # 通过文本精确定位
    driver.find_element_by_link_text("text_vaule")
    # 通过文本模糊定位
    driver.find_element_by_partial_link_text("部分text_vaule")

def css(): # css的速度比xpath快
    driver.find_element_by_css_selector("#id") # id属性定位
    driver.find_element_by_css_selector(".class_value") # class属性定位
    driver.find_element_by_css_selector("input") # 根据标签名定位
    # 常用
    driver.find_element_by_css_selector("[name='xx']")
    driver.find_element_by_css_selector("[maxlength='223']")
    #属性包含某个值 适用于空格分割的属性值 (常用)
    driver.find_element_by_css_selector("[name~='wd']")

    driver.find_element_by_css_selector("span>input") # 父子定位元素
    # 组合定位元素
    driver.find_element_by_css_selector("input#kw") # input标签下属性为kw的元素
    driver.find_element_by_css_selector("input.s_ipt") # input 标签下，class为s_ipt的元素
    driver.find_element_by_css_selector("input[name='wd']") # input标签下name属性为wd的元素
    driver.find_element_by_css_selector("span>input.s_ipt") # span下的input标签下的class属性为s_ipt的元素

    # 多个属性组合
    driver.find_element_by_css_selector("input.s_ipt[name='wd']") # input标签下class为s_ipt的所有元素下name=wd的元素
    #input标签下name属性为wd且maxlength为255的元素
    driver.find_element_by_css_selector("input[name='wd'][maxlength='255']")
