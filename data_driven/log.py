# -*- coding: utf-8 -*-
#@Author : Wu
#@Time : 2017/8/21 11:00
#@File : log.py
#@remark : log 配置

import logging
from data_driven.comhandle import *

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt= '%d %b %H:%M:%S',
        filename= ComHandle().DATA_DIRS()+'\\super.log'
    )
def log(msg):
    logging.info(msg)
    logging.info("*******************")

    '''logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s[line:%(lineno)d] %(message)s ',
        datefmt= '%d %b %H:%M:%S',
        filename= ComHandle().DATA_DIRS()+'\\super.log',
        filemode='w'
    )
    logging.basicConfig(
        level=logging.ERROR,
        # format= '%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        format='%(filename)s[line:%(lineno)d] %(message)s ',
        datefmt= '%d %b %H:%M:%S',
        filename= ComHandle().DATA_DIRS()+'\\super.log',
        filemode='w'
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(filename)s[line:%(lineno)d] %(message)s ',
    datefmt= '%d %b %H:%M:%S',
    filename=ComHandle().DATA_DIRS()+'\\super.log',
    filemode='w'
)'''
