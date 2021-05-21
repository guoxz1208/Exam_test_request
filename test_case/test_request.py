#-*- coding: utf-8 -*-
#@File    : test_request.py
#@Time    : 2020/10/26 21:29
#@Author  : xintian
#@Email   : xx@qq.com
#@Software: PyCharm


import os,sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
from common.get_log import get_log
logger =get_log()
import pytest
# class Test_sq:
#     def test_001(self):#用例函数
#         print('---开始执行---')
#         assert 1+1 == 1
#         print('---结束执行---')
#
#     def test_002(self):#用例函数
#         print('---开始执行---')
#         assert 1+1 == 2
#         print('---结束执行---')
from tools.ExcelDataCtl import get_excel_data
from lib.apiLib.login import Login
from lib.apiLib.msg import Msg
#1- 获取excel数据---请求体+预期结果
# resList = get_excel_data('1-登录模块','login')
#2- 数据传入接口代码--请求体
#3- 写入测试结果  pass/fail   预期结果与实际结果对比
# testData={'username': '20154084', 'password': '123456'}
#1- 登录的测试类
'''
从excel获取请求体/响应的预期结果
'''
class TestLogin:
    #get_excel_data('1-登录模块','login')---[(),()]
    @pytest.mark.parametrize('CaseName,inBody,expData',get_excel_data('1-登录模块','login'))#数据驱动---如果自己开发--一定会写一个for
    def test_login(self,CaseName,inBody,expData):
        #2- 调用登录的接口代码
        logger.info("\n ==========【登录】测试用例开始 ==========:"+str(CaseName))
        res = Login().login(inBody,getToken=False)#获取响应数据---字典格式
        #3- 预期结果--excel里与实际结果对比
        logger.info('\n ----------【实际结果】 ----------:'+str(res))
        logger.info('\n ----------【预期结果】 ----------:' + str(expData))
        assert res['message'] == expData['message']

class TestSelect:
    @pytest.mark.parametrize('CaseName,inBody,expData',get_excel_data('1-登录模块','select'))
    def test_select(self,CaseName,inBody,expData):
        logger.debug("\n ==========【查询】测试用例开始 ==========:"+str(CaseName))
        res = Msg().add_msg(inBody,getToken=True)
        logger.debug('\n ----------【实际结果】 ----------:' + str(res))
        logger.debug('\n ----------【预期结果】 ----------:' + str(expData))
        try:
            assert res['message'] == expData['message']
        except:
            logger.debug("\n ==========【查询】用例失败,预期结果与实际结果不一致==========")
            assert False




if __name__ == '__main__':
    #1- 框架执行后的结果数据  --alluredir

    # pytest.main(['test_request.py','-s','--alluredir','../report/tmp'])
    #2- 使用allure  应用，去打开这个结果数据-并且 浏览器访问（使用火狐/谷歌--设置默认浏览器）
    # os.system('allure serve ../report/tmp')

    pytest.main(['-s', "--html="+base_path +"/report/html/report"+nowTime+".html", 'test_request.py'])
    '''
    -s  控制台显示打印信息
    F ---断言失败
    E   有异常
    .  成功
    '''

