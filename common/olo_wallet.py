# coding:utf-8
# @author : csl
# @date   : 2018/07/04 15:01
# 获取olo钱包注册用户

import requests
import json
from common.operateExcel import operateExcel

requrl = "http://192.168.8.163:8000/v1/genkey"
datapath = "D://keysAPI.xlsx"
resultdatas = []
for i in range(0,1200):
    reqresult = requests.get(requrl)
    # reqdata = eval(reqresult.text)
    reqdata = json.loads(reqresult.text)
    # print(type(reqdata))
    reqdatas = [reqdata["result"]["privkey"], reqdata["result"]["address"]]
    resultdatas.append(reqdatas)
print("开始保存数据")
operateExcel().write_07_Excel(datapath, resultdatas)
# print(resultdatas)
print("保存成功")