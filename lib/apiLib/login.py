#-*- coding: utf-8 -*-
#@File    : login.py
#@Time    : 2020/10/26 20:22
#@Author  : xintian
#@Email   : xx@qq.com
#@Software: PyCharm
#1- 完成登录代码的编写---依据接口文档
from configs.config import HOST
import requests
import pprint#完美打印
import hashlib


#发请求
'''
data---一般是表单
json---  json格式
files---文件
'''

# pprint.pprint(resp.json())
# print(resp.request.headers)#请求头

'''
封装思路：
    1- 登录接口比较特殊
        用途：
            1- 获取登录的token----给后续接口做关联
            2- 接口本身也需要自动化测试
'''
def get_md5(psw):#加密=函数
    md5 = hashlib.md5()#创建md5对象
    md5.update(psw.encode('utf-8'))#加密方法
    return md5.hexdigest()#加密后的结果

class Login:#登录类
    def login(self,inData,getToken=False):#实例方法
        # 1- 接口的url---考虑参数化
        url = f'{HOST}/api/login'  # 字符串
        # print(url)
        # 2-构建请求
        payload = inData# 请求体 body
        # payload['password']=get_md5(payload['password'])#字典--修改值的操作
        #字典修改值操作：  字典名[键名]=新的值
        resp = requests.post(url, json=payload)
        # print(resp.json())
        if getToken:#获取token
            return resp.json()['data']['token']
        else:
            return resp.json()# 返回是字典格式

if __name__ == '__main__':
    testData={"username": "admin", "password": "123456"}
    #实例化对象
    res=Login().login(testData,getToken=True)
    print(res)

