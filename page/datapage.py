# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:58
#@File : datapage.py
#@remark : 数据模块
from selenium.webdriver.common.action_chains import ActionChains
from  page.compage import  *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

item_list = {"销量":"saleCount","收藏量":"save","销售额":"amount",
             "新增产品数量":"newCount"}

class DataPage():

    def __init__(self,driver):
        self.dr = driver

 # tab页切换通用 -start
    def tab_click(self,tab_name):
        try:
            nav = self.dr.find_element_by_class_name("tab-nav")
            tab = nav.find_element_by_xpath("//div[contains(text(),'"+tab_name+"')]")
            tab.click()
            sleep(1)
            return "True:进入"+tab_name+"-成功"
        except:
            text = ComPage(self.dr).get_alert_value()
            return "False:进入"+tab_name+"-失败-"+text
# tab页切换通用 -end

# 选择行业切换 -start level_1  一级菜单  2 二级菜单
    def industry_click(self,level_1,level_2):
        # industry = self.driver.find_element_by_class_name("industry-popup-container")
        left = self.dr.find_element_by_id("menu-container")
        one = left.find_element_by_xpath("//li[contains(text(),'"+level_1+"')]")
        ActionChains(self.dr).move_to_element(one).perform()
        right = self.dr.find_element_by_id("panel-container")
        two =right.find_element_by_xpath("//div[contains(text(),'"+level_2+"')]")
        two.click()

# 选择行业切换 -end

# 日期控件选择操作 -start - 暂时只支持7天30天切换
    def date_change(self,type_num,date=""):
        daterange = self.dr.find_element_by_class_name("daterange")
        if type_num == "7天" or type_num=="30天":
            daterange.find_element_by_css_selector("input[data-range='"+type_num+"'").click()
        else:
            pass
# 日期控件选择操作 -end

# 全局分析及检索 -start
class AnalysisPage(DataPage):

# 获取所选行业的detail各项数据 -start
    def get_wish_data(self):
        data_result = {}
        detail = self.dr.find_element_by_class_name("detail-container")
        divs = detail.find_elements_by_class_name("box")
        for div in divs:
            title = div.find_element_by_class_name("title").text
            content =  div.find_element_by_class_name("content").text
            data_result[title]=content

        return data_result

# 获取所选行业的detail各项数据 -end
# 获取行业概况图标数据 -START
    #图表切换 amount-销售额/save-收藏量/newCount-新增产品数量/saleCount-销量
    def cat_tab(self,tab_name):
        chart = self.dr.find_element_by_class_name("chart-thumbnail")
        if ComPage(self.dr).wait_element(chart.find_element_by_name(item_list[tab_name])):
            chart.find_element_by_name(item_list[tab_name]).click()
        sleep(1)

    def get_cat_data(self):
        data_result = []
        g = self.dr.find_element_by_css_selector("g.highcharts-markers.highcharts-tracker")
        paths = g.find_elements_by_tag_name("path")
        for i in range(0, paths.__len__())[::-1]:
            ActionChains(self.dr).move_to_element(paths[i]).perform()
            sleep(0.5)
            value = self.dr.find_elements_by_tag_name("tspan")[3].text
            data_result.append(value)
            # sleep(0.5)
        return data_result

# 获取行业概况图表数据 -end
# 获取子行业概况数据 -start
    # 选择对比数据类型
    def sub_contrast(self,data_name):
        radio = self.dr.find_element_by_class_name("radio-container")
        # radio.find_element_by_xpath("//div[contains(text(),'"+data_name+"')]").click() # 这里定位有问题
        radio.find_element_by_xpath("//input[@data-type='"+item_list[data_name]+"']").click()
        sleep(1)

    # 右侧列表数据
    def get_sub_data(self):
        sub_result = {}

        table = self.dr.find_element_by_css_selector("div.right.table")
        trs_1 = table.find_elements_by_tag_name("tr")
        del trs_1[0] # 删除表头
        # trs_1 = trs_1.pop(0) # 剔除第一个表头元素
        for trs in trs_1:
            sub_value =[]
            tds = trs.find_elements_by_tag_name("td")
            name = trs.find_element_by_class_name("erp-ellipsis").text
            sales =  tds[2].text
            scale = tds[3].text
            sub_value.append(sales)
            sub_value.append(scale)
            sub_result[name]=sub_value

        com = ComPage(self.dr)
        number = com.get_all_page()
        if number >1:
            for x in range(1,number):
                com.to_page(3)
                table = self.dr.find_element_by_css_selector("div.right.table")
                trs_2= table.find_elements_by_tag_name("tr")
                del trs_2[0] # 剔除第一个表头元素
                for trs in trs_2:
                    sub_value =[]
                    tds = trs.find_elements_by_tag_name("td")
                    name = trs.find_element_by_class_name("erp-ellipsis").text
                    sales =  tds[2].text
                    scale = tds[3].text
                    sub_value.append(sales)
                    sub_value.append(scale)
                    sub_result[name]=sub_value

        return sub_result

# 获取子行业概况数据 -end

# 店铺检索、产品检索 -start
class SearchPage(DataPage):

    # 店铺-搜索内容输入-搜索
    def shop_search(self,content):
        text = self.dr.find_element_by_name("search-value")
        text.send_keys(content)
        text.send_keys(Keys.ENTER)
        # 为了防止样式变化，使用回车搜索

    # 店铺、产品页面点击采集、关注
    def shop_follow(self,button_name):
        button = self.dr.find_element_by_id("BUTTON-CONTAIENER")
        button.find_element_by_link_text(button_name).click()

    # 获取table 表头名称 // 不通用，数据模块与其他的不一致
    def get_table_name(self):
        nameList =[]
        header = self.dr.find_element_by_class_name("trade-header")
        ths = header.find_elements_by_tag_name("th")
        for num in range(2,len(ths)):
            title = ths[num].find_element_by_class_name("title")
            nameList.append(title)

    #获取一行列表数据,目前只考虑主流程校验，如需要数据校验，可以直接解析json返回
    def col_data(self,num="",type=""):
        if type == "ALL":
            pass


    # 获取当前数据是否被关注\有无货源\有无采集,element 需要传入整个tr元素，num表示哪个td
    def is_follow(self,num=0,is_have=u"已关注"):
        follow_list = []
        try:
            tr =self.return_tr(num)
            td = tr.find_elements_by_tag_name("td")[2]
            follow = td.find_elements_by_class_name("tag")
            for tag in follow:
                value = tag.text
                follow_list.append(value)

            if is_have in follow_list:
                return True
            else:
                return False
        except NoSuchElementException as e :

            print(str(sys.exc_info()))
            pass


    def return_tr(self,num=0):
        return self.dr.find_elements_by_class_name("item-tr")[num]

    # 数据选中
    def data_pitch_on(self,num):
        self.dr.find_elements_by_class_name("item-tr")[num].click()

    # 名称点击打开详情页
    def name_click(self,num=0):
        try:
            tr =self.return_tr(num)
            td = tr.find_elements_by_tag_name("td")[2]
            name = td.text
            td.find_element_by_class_name("item-name").click()
            return "True:"+ name +"打开详情页"
        except:
            text = ComPage(self.dr).get_alert_value()
            return u"False:打开详情页失败,"+text

    # 产品数量点击打开产品搜索自定义列表
    def shop_to_goods(self,num=0):
        tr =self.return_tr(num)
        td = tr.find_elements_by_tag_name("td")[3]
        td.find_element_by_tag_name("a").click()


    # 产品页面采集进度弹出框
    def gathering(self):
        pass

    # 产品关注弹出框确认
    def concern(self):
        self.dr.find_element_by_class_name("ui_state_highlight").click()

# 店铺检索、产品检索 -end

# 店铺详情页、产品详情页 -start
class DetailPage(DataPage):

   # 店铺详情页-与产品详情页的html结构不一致,可以成功失败获取弹出框内容
    def shop_follow(self):
        try:
            shop_name = self.dr.find_element_by_class_name("item-name").text
            self.dr.find_element_by_css_selector("span.btn.btn-success.J_focus").click()
            success = ComPage(self.dr).get_alert_value()
            return "True:"+shop_name+"，"+success

        except:
            error = ComPage(self.dr).get_alert_value()
            return "False:店铺详情页关注失败"+error

#------产品详情页 start ----
    # 没有弹出框
    def goods_follow(self):
        self.dr.find_element_by_css_selector("div.btn.btn-success").click()

    # 采集产品到本地/可以成功失败弹出框
    def primary_goods(self):
        self.dr.find_element_by_css_selector("div.btn.btn-primary").click()

    # 前往产品查看
    def go_to_product(self):
        self.dr.find_element_by_class_name("J_goto-product").click()
#------产品详情页 end ----

# 店铺、产品详情页 -end

