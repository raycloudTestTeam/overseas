# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 17:23
#@File : excelhandle.py
#@remark :excel 的操作集合

import xlrd
import sys

class ExcelHandle(object):

    def open(self,file):
        try:
            workbook = xlrd.open_workbook("../data_driven/file_path/%s.xlsx" % file,formatting_info=True) # , formatting_info=True
            return workbook # 转换文件对象，方便操作
        except :
            print(sys.exc_info())
            #logging 记录点
            print("打开文件失败,检查文件是否打开")
    # 获取单元格内容
    def read_cell(self,sheet,iRow,iCol):
        try:
            value = sheet.cell_value(iRow - 1,iCol - 1)  # 获取响应的单元格的值
            return value
        except:
            print("读取单元数据失败:%s"% str(sys.exc_info()))

    # 单元格写入
    def write_cell(self,sheet,iRow,iCol,iData=""):
        try:
            sheet.write(iRow,iCol,iData)
        except:
            print("写入单元数据失败: %s"% str(sys.exc_info()))

    def save(self,book,iPath):
        try:
            book.save(iPath)
        except:
            print("文件保存失败:%s"% str(sys.exc_info()))

    # 获取sheet数量
    def get_sheet_count(self,book):
        return len(book.sheets())

    def get_num(self,sheet,type="rows"):
        if type =="rows":
            return sheet.nrows - 1
        else:
            return sheet.ncols - 1

    # 获取sheet对象,copy 与 没有copy下的获取
    def ret_sheet(self,book,num):
        try:
            return book.sheet_by_index(num)
        except:
            return book.get_sheet(num)