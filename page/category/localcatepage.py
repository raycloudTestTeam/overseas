# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/24 10:26
#@File : localcatepage.py
#@remark : 本地数据页面
from page.category.catebasepage import *

class LocalCatePage(CateAction):

#采集产品相关操作　－－start

    # 采集产品按钮点击
    def collect_click(self):
        self.find_ele(By.CSS_SELECTOR,"button.btn.J_collect_directly.mr_5").click()

    #采集url输入
    def url_input(self):
        url = "" # url 从url文件中读取
        textarea = self.find_ele(By.NAME,"url")
        textarea.click()
        textarea.send_keys(url)

    # 点击开始采集按钮
    def start_collect_click(self):
        self.find_ele(By.XPATH,"//span[@data-type='start']").click()


    def collect(self):
        try:
            pass

        except:
            log(u"采集失败:"+self.alert_msg())





#采集产品相关操作　－－end