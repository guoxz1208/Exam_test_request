#-*- coding: utf-8 -*-
#@File    : ExcelDataCtl.py
#@Time    : 2020/10/26 21:35
#@Author  : xintian
#@Email   : xxx@qq.com
#@Software: PyCharm
import xlrd
from xlutils.copy import copy
import json
#字典--存储结构
# json  字符串
#1- 获取excel数据---请求体+预期结果
def get_excel_data(sheetName,caseName):
    '''
    :param sheetName: 表名
    :param caseName: 用例名
    :return: 一个列表嵌套元组   [(请求体1，期望数据1),(请求体2，期望数据2)]
    '''
    resList = []#放结果的
    excelDir = '../data/在线考试系统接口测试用例-v1.3.xls'
    #1- 打开excel对象---formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #2- 对某一个sheet操作
    workSheet = workBook.sheet_by_name(sheetName)
    #3- 获取值  第6列 和第8列
    # print(workSheet.col_values(0))

    #4- 获取数据
    idx = 0#从第0行开始操作-也可以从第1行（根据实际sheet）
    for one in workSheet.col_values(0):
        if caseName in one:#说明这条用例使我们需要的
            #请求体--单元格数据--cell(行号，列号)0从0开始
            reName = workSheet.cell(idx,1)
            reqBody = workSheet.cell(idx,6).value
            respData = workSheet.cell_value(idx, 8)#期望数据
            #每一行数据增加返回list里
            # 字符串--转化--字典  字典 = json.loads(json数据)
            resList.append((reName,json.loads(reqBody),json.loads(respData)))#字符串格式--不能使用键去取值

            #[('',''),()]
        idx += 1#每次遍历一次，就准备操做下一行
    return resList



if __name__ == '__main__':
    res = get_excel_data('1-登录模块','login')
    for one in res:
        print(one)
