#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from common.handle_excel import HandleExcel
import os,sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

class ExcelData:

    def __init__(self):
        self.excel_data = HandleExcel()

    def excle_text(self):
        resList = []
        res = self.excel_data.all_data_excel()
        for test in res:
            data = test
            casename = data[0]
            method = data[4]
            header = data[5]
            resBaby = data[6]
            respData = data[8]
            get_cookie = data[9]
            get_token = data[10]
            resList.append((casename,method,header,resBaby,respData,get_cookie,get_token))

        return resList


if __name__ == '__main__':
    data = ExcelData()
    test = data.excle_text()
    for one in test:
        print(one)