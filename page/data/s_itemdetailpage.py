# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 15:14
#@File : s_itemdetailpage.py
#@remark : 产品详情页  (拼接url进入页面)-作废

from page.data.databasepage import *
class SItemDetailPage(DataAction):

    def open_url(self,item_id):
        try:
            js = "window.open('https://overseas.superseller.cn/index.html#/data_shopee/shop_detail/?shopId="+item_id+"')"
            self.driver.execute_script(js)
            self.driver.close()
            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(1)
        except:
            log(u"打开产品详情页失败：%s" %self.alert_msg())
            print(str(sys.exc_info()))
    #
    def button_check(self,name):
        try:
            buttons = self.find_ele(By.CLASS_NAME,"breadcrumb")
            con = buttons.find_element_by_class_name("button-container")
            if name == u"前往产品查看":
                con.find_element_by_class_name("J_goto-product").click()
            elif name ==u"关注产品":
                con.find_element_by_css_selector("div.btn.btn-success").click()
                sleep(1)
                log(u"产品关注："+self.alert_msg())
            elif name == u"采集到本地":
                con.find_element_by_css_selector("div.btn.btn-primary").click()
                sleep(0.5)
                ui_content = self.driver.find_element_by_class_name("ui_content")
                title = ui_content.find_element_by_class_name("title").text
                log(title)
                ui_content.find_elements_by_tag_name("span")[1].click()
                sleep(0.5)
                log(self.alert_msg())
            else:
                con.find_element_by_css_selector("div.btn.btn-cancel").click()
                log(self.alert_msg())
            # log(u"产品详情页：%s--点击" % name)
            sleep(1)
        except:
            log(u"产品详情页：%s，报错：%s" % (name,self.alert_msg()))

