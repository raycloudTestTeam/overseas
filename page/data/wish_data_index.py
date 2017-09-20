# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/9/20 14:24
#@File : wish_data_index.py
#@remark : 全站分析页面
from page.data.wish_data import *
class WishDataIndexPage(WishDataAction):

    # wish产品 -start
    def product_all_table(self):
        all_value ={}
        tds = self.driver.find_elements_by_css_selector("[class~='product-all-table'] td")
        for td in tds:
            spans = td.find_elements_by_tag_name("span")
            name = spans[0].text
            value = spans[1].text
            if "万" in value:
                value = value.replace('万','0000')
            all_value[name]=value
        print(str(all_value))
        return all_value

    # 返回7日销量分析的所有元素
    def product_amount7_table(self):
        amount7 = self.driver.find_elements_by_css_selector("[class~='product-amount7-table'] li")
        return amount7

    # 获取销量分析数据
    def get_amount7_table(self,ty=1):
        amount7_all ={}
        if ty ==1:
            for li in self.product_amount7_table():
                divs_value = li.find_elements_by_tag_name("div")
                amount7_all[divs_value[0].text] = str(divs_value[1].text+","+divs_value[2].text)
            print(str(amount7_all))
            return amount7_all
        else:
            # ty==2 则存入操作查看产品的元素
            for li in self.product_amount7_table():
                divs_value = li.find_elements_by_tag_name("div")
                amount7_all[divs_value[0].text] = divs_value[3]
            return amount7_all


    def open_amount7_product(self,content):
        if content == ">500":
            content = "销量"+content
        else:
            content = "销量在"+content+"之间"
        try:
            open_all = self.get_amount7_table(ty=2)
            open_one = open_all[content].find_element_by_tag_name("a")
            open_one.click()
            print(content +"点击成功")
        except:
            print(str(sys.exc_info()))
            log(u"Wish产品-产品7日销量分析-%s 查看产品失败" % content)

    # wish产品 -end

    # wish店铺 -start
    # wish店铺 -end