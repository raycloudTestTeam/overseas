# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:57
#@File : txthandle.py
#@remark : txt文件操作相关
import random
from data_driven.comhandle import *
import logging
import sys
import types
class TxtHandle(object):

    # 读取txt
    def read_txt(self,filename):
        txt_result = []
        if filename =="":
            print(u"文件名不能为空")
        else:

            file = open(ComHandle().DATA_DIRS()+"\\%s.txt" %filename)
            for line in  file:
                txt_result.append(line)
            file.close()
            return txt_result

    # 写入txt 1覆盖写入，2不覆盖写入
    def write_txt(self,filename,content,t=1):
        try:
            if content =="":
                return False
            else:
                file = open(ComHandle().DATA_DIRS()+"\\%s.txt" %filename,'w')
                if t == 1:
                    if isinstance(content,list):
                        for i in content:
                            file.write(i)
                            file.write(",")
                    else:
                        file.write(content)
                    file.close()
                else:
                    pass
                return True
        except:
            print(str(sys.exc_info()))
            return False




if __name__ =="__main__":
    pass