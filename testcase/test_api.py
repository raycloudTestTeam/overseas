# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 17:21
#@File : test_api.py
#@remark : 跨境接口自动化测试

import  unittest
from data_driven.excelhandle import *
import requests
from xlutils.copy import copy
import dingtalk
from time import sleep
from login import *
from driver import *
# 待验证
class Seller_Api(unittest.TestCase):

    def setUp(self):
        self.file ="sellerapi"
        self.excel = ExcelHandle(self.file)
        self.title_index = 3 # 用例标题
        self.case_index = 4 # 测试用例开始下标
        self.arg_index_y = 2 # 传递参数开始位置下标

        self.driver = Driver(url="",browser="HtmlUnit").start()
        self.driver.get("http://overseas.superseller.cn/index.html#/index/work/")
        sleep(0.5)
        self.driver.maximize_window()
        Login(self.driver).login()
        sleep(2)

    #获取单个sheet的用例数
    def get_case_count(self,sheet):
        try:
            n_rows = sheet.nrows
            case_count = n_rows - self.case_index + 1
            if case_count > 0:
                return case_count
            else:return 0
        except:
            print(sys.exc_info())
            return 0

    #获取参数名
    def get_arg_name(self,book,sheetId):
        arg_name = []
        sheet = book.sheet_by_index(sheetId)

        self.arg_count = int(self.excel.read_cell(sheet,2,2))
        self.case_count = int(self.get_case_count(sheet))
        self.interface = self.excel.read_cell(sheet,1,2)
        self.method = self.excel.read_cell(sheet,2,7) # 传递方式
        self.result_col = sheet.ncols -1
        self.status_col = sheet.ncols -2
        self.re_url = sheet.ncols - 3
        for ar in range(0,self.arg_count):
            arg_name.append(self.excel.read_cell(sheet,self.title_index,self.arg_index_y+ar))
        return arg_name

    # 将 参数名与值 组合成dict{arg_name:argValue}
    def get_arg_value(self,book,sheetId,caseId,arg_name):
        value = [] # 每一行的case_arg_name 对应的值
        arg_name_value = {}
        sheet = book.sheet_by_index(sheetId)
        for j in range(self.arg_index_y,self.arg_index_y + len(arg_name)):
            arg_value = self.excel.read_cell(sheet,self.case_index + caseId,j)
            if isinstance(arg_value,float):
                value.append(int(arg_value))
            else:
                value.append(arg_value)

        for num in range(0,len(arg_name)):
            arg_name_value[arg_name[num]] = value[num]

        return arg_name_value #[arg_name:arg_value]

    # 校验json 返回 result状态码 （这里可以写成相应项目的返回）
    def HttpInvoke(self,inter,load):
        try:
            if self.method == "POST":
                ep = requests.post(inter,data=load)
                rep = ep.json()
                rep_statue = rep["result"]
                if rep_statue == 100:
                    result = (str(ep.url)+","+str(rep_statue)+",OK")
                else:
                    result = (str(ep.url)+","+str(rep_statue)+",NG")
                return result  # [返回状态，测试结果]
            else:
                # 做一个登陆信息的
                op = requests.get(inter,params=load)
                re = op.json()
                re_statue = re["result"]

                if re_statue == 100:
                    result = (str(op.url)+","+str(re_statue)+",OK")
                else:
                    result = (str(op.url)+","+str(re_statue)+",NG")
                return result  # (返回状态，测试结果)
        except:
            print(sys.exc_info())
            result = (""+",链接打开失败"+",NG")
            return result

    # 写入相应的测试结果
    def re_write(self,sheetId,caseId,data):
        book = self.excel.open()
        workbook = copy(book)
        sheet = workbook.get_sheet(sheetId)
        row = self.case_index + caseId -1
        re = data.split(",")
        sheet.write(row,self.re_url,re[0])
        sheet.write(row,self.status_col,re[1])
        sheet.write(row,self.result_col,re[2])
        workbook.save(self.file)

    # 开始用例
    def test_run(self):
        all_result = []
        book = self.excel.open()
        # 获取sheet数量
        sheets = self.excel.get_sheet_count(book)
        if sheets == 1:
            arg_name_list = self.get_arg_name(book,0)
            for case in range(0,self.case_count):
                arg_value_dict = self.get_arg_value(book,0,case,arg_name_list)
                result = self.HttpInvoke(self.interface,arg_value_dict)
                self.re_write(0,case,result)

        else:
            for she in range(0,sheets):
                arg_name_list = self.get_arg_name(book,she)
                for case in range(0,self.case_count):
                    arg_value_dict = self.get_arg_value(book,she,case,arg_name_list)
                    result = self.HttpInvoke(self.interface,arg_value_dict)
                    self.re_write(she, case,result)
        dingtalk.ding_talk("接口用例已经跑完",0)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2)