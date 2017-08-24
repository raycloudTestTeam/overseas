# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 15:12
#@File : s_shopdetailpage.py
#@remark : 店铺详情页
from page.data.databasepage import *

class SShopDetailPage(DataAction):

    def open_url(self,shop_id):
        try:
            js = "window.open('https://overseas.superseller.cn/index.html#/data_shopee/shop_detail/?shopId="+shop_id+"')"
            self.driver.execute_script(js)
            self.driver.close()
            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(1)
        except:
            log(u"打开店铺详情页失败：%s" %self.alert_msg())
            print(str(sys.exc_info()))

    # 详情页-关注取消按钮点击
    def button_check(self,name):
        try:
            buttons = self.find_ele(By.CSS_SELECTOR,"div.f-rt.top-button-container")
            buttons.find_element_by_xpath("//span[contains(text(),'"+name+"')]").click()
            log(u"店铺详情页：%s-成功" %name)
        except:
            log("店铺详情页报错：%s" % self.alert_msg())