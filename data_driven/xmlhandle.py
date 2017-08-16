# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/16 17:53
#@File : xmlhandle.py
#@remark : xml操作相关

import  xml.dom.minidom

class XmlHandle(object):

    def open(self,file):
        return xml.dom.minidom.parse("../data_driven/file_path/%s.xml" % file)

    # 获取某个tag的元素集合
    def get_elements(self,file,tag_name):
        xm = xml.dom.minidom.parse("../data_driven/file_path/%s.xml" % file)
        root = xm.documentElement
        itemList = root.getElementsByTagName(tag_name)
        return itemList

    # 获取某个tag的属性值
    def get_item_value(self,tag,item_name):
        value = tag.getAttribute(item_name)
        return value
