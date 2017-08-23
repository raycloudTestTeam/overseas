# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 18:42
#@File : comhandle.py
#@remark : 其他的一些通用操作集合
import os

class ComHandle(object):

    def DATA_DIRS(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIRS = (os.path.join(BASE_DIR,'data_driven\\file_path'))
        return DATA_DIRS