# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/20 14:24
#@File : wish_data_index.py
#@remark : 全站分析页面
from page.data.wish_data import *
class WishDataIndexPage(WishDataAction):
    # wish产品/店铺统计 -start

    # wish产品/店铺统计数据
    def all_count(self,table_type):
        all_value ={}
        tds = self.driver.find_elements_by_css_selector("[class~='"+table_type+"-all-table'] td")
        for td in tds:
            spans = td.find_elements_by_tag_name("span")
            name = spans[0].text
            value = spans[1].text
            if "万" in value:
                value = value.replace('万','0000')
            all_value[name]=value
        print("wish全站 %s 统计\n"%table_type+str(all_value)+"\n----")
        return all_value

    # 产品/店铺 7日销量分析的所有元素
    def product_amount7_table(self,table_type):
        '''
        table_type:     shop-wish店铺  product-wish产品
        '''
        amount7 = self.driver.find_elements_by_css_selector("[class~='"+table_type+"-amount7-table'] li")
        return amount7

    # 产品/店铺7日数据元素
    def amount7_table(self,table_type,data_type=1):
        '''
        :data_type 1-获取名称、销量值、比例值   2-查看产品元素
        :return dict[name:total,%]
        '''
        amount7_all ={}
        if data_type ==1:  #获取统计数据
            for li in self.product_amount7_table(table_type):
                divs_value = li.find_elements_by_tag_name("div")
                amount7_all[divs_value[0].text] = str(divs_value[1].text+","+divs_value[2].text)
            print("%s-7日销量分析\n"%table_type+str(amount7_all)+"\n-----")
            return amount7_all
        else:
            for li in self.product_amount7_table(table_type):
                divs_value = li.find_elements_by_tag_name("div")
                amount7_all[divs_value[0].text] = divs_value[3]
            return amount7_all

    # 点击查看店铺/查看产品-跳转列表打开页面
    def open_amount7_entry(self,content,table_type):
        if ">" in content:
            content = "销量"+content
        else:
            content = "销量在"+content+"之间"
        try:
            open_all = self.amount7_table(table_type,2)
            open_one = open_all[content].find_element_by_tag_name("a")
            open_one.click()
            print("%s:"%table_type+content +"查看产品跳转")
        except:
            print(str(sys.exc_info()))
            #log(u"Wish产品-产品7日销量分析-%s 查看产品失败" % content)

    # wish产品/wish店铺 -end
    # wish行业 -start