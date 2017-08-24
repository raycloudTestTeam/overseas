# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 15:14
#@File : s_itemdetailpage.py
#@remark : 产品详情页  (拼接url进入页面)

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
            else:
                con.find_element_by_xpath("//div[contains(text(),'"+name+"')]").click()
            log(u"产品详情页：%s--点击" % name)
            sleep(1)
        except:
            log(u"产品详情页：%s，报错：%s" % (name,self.alert_msg()))

