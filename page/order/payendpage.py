# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 10:39
#@File : payendpage.py
#@remark : 待处理订单

from page.order.orderbasepage import *
class PayEndPage(OrderAction):

    tool_dic={u"合并订单":"J_merge-order",
               u"拆分订单":"J_split-order",
               u"导出订单":"J_out-order",
               u"新建订单":"J_new-order",
               u"放入回收站":"J_delete-order"}

    order_list ={"buyerId":"19921106","buyerNick":"TestTeamWu","receiverName":"TestTeamWu"
                    ,"receiverCompany":"Raycloud","phone":"132152000",
                     "state":"Zhejiang","city":"HangZhou","streetAddress1":"宇宙街xx","zipCode":"3180",
                 "buyerEmail":"test@test.com","totalPrice":"",
                     "logisticsAmount":"","breakPrice":"","taxes":""}

    sku_list={"sku":"sku_name","title":"title_name","price":"","quantity":""}

    # 更多按钮点击
    def more_button(self,name):
        #toolbar =  self.driver.find_element_by_class_name("fixed-toolbar")
        self.find_elem(self.driver.find_element_by_xpath
                       ("//button[contains(text(),'更多') and @data-toggle='dropdown']")).click()
        btn = self.find_elem(self.driver.find_element_by_class_name(self.tool_dic[name]))
        btn.click()

    # 新建订单操作
    def create_order(self):
        try:
            self.more_button(u"新建订单")
            # 随机加两位
            for (ele, value) in self.order_list.items():
                te = self.find_elem(self.driver.find_element_by_name(ele))
                if ele =="buyerEmail":
                    te.send_keys(str(value))
                else:
                    te.send_keys(str(value+str(random.randint(10,99))))
            new_pro = self.find_elem(self.driver.find_element_by_css_selector("span[class~='J_add']"))
            new_pro.click()
            for (sku_ele,sku_value) in self.sku_list.items():
                sku =  self.find_elem(self.driver.find_element_by_name(sku_ele))
                sku.send_keys(str(sku_value+str(random.randint(10,99))))

            save = self.find_elem(self.driver.find_element_by_css_selector("span[class~='J_save']"))
            save.click()
        except:
            print(str(sys.exc_info()))
            print(u"新建订单失败")
            log(u"新建订单失败")

    # 订单放入回收站操作
    def delete_order(self):
        try:
            self.more_button(u"放入回收站")
            self.make_ok()
            log(u"订单放入回收站成功")
        except:
            print(u"订单放入回收站失败")
            log(u"订单放入回收站失败")