#-*- coding: utf-8 -*-
#@File    : msg.py
#@Time    : 2020/10/26 21:14
#@Author  : xintian
#@Email   : xxx@qq.com
#@Software: PyCharm

#增加留言
import requests
from configs.config import HOST
from lib.apiLib.login import Login
#1- 封装类
class Msg:
    #1- 增加留言
    def add_msg(self,inData,getToken=True):
        '''
        :param inToken: 登录接口获取的token
        :param inData: 留言新增的body
        :return: 响应体
        '''
        if getToken == True:
            token = Login().login({'username': 'admin', 'password': '123456'}, getToken=True)
            header = {'token': token, 'Content-Type': 'application/json'}
        else:
            Login().login({'username': 'admin', 'password': '123456'}, getToken=False)
            header = {'Content-Type': 'application/json'}
        url = f'{HOST}/api/mAlarmHistory/getPageList'
        #请求头--需要带token---格式是字典  {键：值}
        # header = {'token':inToken,'Content-Type':'application/json'}
        payload = inData
        resp = requests.post(url,json=payload,headers=header)
        return resp.json()

#测试下
if __name__ == '__main__':
    #1- 登录操作--获取token
    # token = Login().login({'username': 'admin', 'password': '123456'},getToken=True)
    #2- 新增留言接口
    info = {'pageIndex': 1, 'pageSize': 14, 'startTime': '', 'endTime': '', 'cameraParams': [], 'controlIds': [1]}
    res = Msg().add_msg(info,getToken=True)
    print(res)#这个留言的id  作为后续的删除 回复操作