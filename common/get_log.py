#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: get_log.py

import sys,os
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import logging.config
import logging


# 读取日志配置文件
def get_log():
    con_log = "../logs/log.conf"
    logging.config.fileConfig(con_log)
    log = logging.getLogger()
    return log

print(get_log())