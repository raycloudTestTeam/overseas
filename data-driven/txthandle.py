# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/7 16:57
#@File : txthandle.py
#@remark : txt文件操作相关

class TxtHandle(object):

    # 读取txt
    def read_txt(self,filename):
        txt_result = []
        if filename =="":
            print(u"文件名不能为空")
        else:
            file = open("app/static/data/%s.txt" %filename)
            for line in  file:
                txt_result.append(line)
            return txt_result

    # 写入txt 1覆盖写入，2不覆盖写入
    def write_txt(self,filename,content,type):
        try:
            if content =="":
                return False
            else:
                file = open("app/static/data/%s.txt" %filename,'w')
                if type == 1:
                    file.write(content)
                else:
                    pass
                return True
        except:
            return False
