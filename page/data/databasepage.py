# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/23 10:36
#@File : databasepage.py
#@remark : 数据模块通用操作类-作废
from page.BasePage import *
from selenium.webdriver.common.by import  By
from data_driven.txthandle import *
from time import sleep
from data_driven.log import *
class DataAction(Action):

    # 查询操作
    def data_search(self,content):
        self.find_ele(By.NAME,"mixedCondition2").send_keys(content)
        sleep(1)

    def data_search_click(self):
        self.find_ele(By.NAME,"mixedCondition2").send_keys(Keys.ENTER)
        sleep(1)

    # 获取table tr 个数
    def table_tr(self):
        table =  self.find_ele(By.CLASS_NAME,"data-simple-table")
        trs = table.find_elements_by_class_name("tr-item")
        return trs

    # table 全选
    def check_all(self):
        self.find_ele(By.NAME,"teamAllId").click()
        sleep(1)



    # 列表操作按钮列表点击
    def focus_items(self,name):
        buttons = self.driver.find_element_by_id("BUTTON-CONTAIENER")
        # buttons = self.find_element(By.ID,"BUTTON-CONTAIENER")
        mi = "button.btn."
        if name == u"关注":
            buttons.find_element_by_css_selector(mi+"btn-success.mr_10.J_focus-items").click()
                # return str(self.alert_msg())
        elif name == u"采集":
            buttons.find_element_by_css_selector(mi+"btn-success.mr_10.J_collect-items").click()

        elif name == u"取消关注":
            buttons.find_element_by_css_selector(mi+"mr_10.J_focus-items").click()
        sleep(1)

        # 产品id、店铺id获取
    def get_id(self,name="goods"):

        if name == "shop":
            shop_list = TxtHandle().read_txt("shopee_shopids")
            shops = str(shop_list[0])
            shop_id = random.sample(shops.split(','),1)
            # logging.INFO(str(shop_id[0]))
            return str(shop_id[0])

        else:
            goods_list =TxtHandle().read_txt("shopee_goodids")
            goods = str(goods_list[0])
            new_item = goods.split(',')
            goods_id = random.sample(new_item,1)
            #new_item.remove(goods_id[0])
            # print(str(new_item))
            # TxtHandle().write_txt("shopee_goodids",new_item,1)
            return str(goods_id[0])


    # 采集弹出框,返回预计采集
    def collect_win(self):
        try:
            win = self.find_ele(By.CLASS_NAME,u"ui_content")
            value = win.find_element_by_class_name("title").text
            log(str(value))
            return str(value)
        except:
            log(u"采集弹出框打开：%s" %self.alert_msg())
            return self.alert_msg()

    # 采集弹出框-确认
    def collect_win_ok(self):
        bottom = self.driver.find_elements_by_tag_name("span")[1]
        bottom.click()

    # 采集进度确定
    def collecting(self):
        while 1:
            try:
                self.persent = self.driver.find_element_by_class_name("persent-num").text
                if "100" in self.persent:
                    context = self.driver.find_element_by_class_name("process-context").text
                    log(str(context))
                    self.driver.find_element_by_xpath("//*[@data-info='close']").click()
                    break
            except:
                # persent = self.driver.find_element_by_class_name("persent-num").text
                log(u"采集失败，采集进度：%s"% self.persent)
                break

    def detail_tab_check(self,name):
        try:
            ul = self.find_ele(By.CSS_SELECTOR,"ul.tab-nav.clearfix")
            tab = ul.find_element_by_xpath("div[contains(text(),u'"+name+"')]")
            tab.click()
            sleep(1)
            log(u"切换%s失败：%s" % (name,self.alert_msg()))
        except:
            print(u"找不到该tab：%s" % name)

