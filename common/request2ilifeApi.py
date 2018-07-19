# coding:utf-8
# @author : csl
# @date   : 2018/07/18 11:00
# 访问i生活Api

from common.base import buApiBase
import requests
import random
import time
import uuid


class request2ilifeApi(object):

    def __init__(self, service, senddata):

        self.service = service
        self.senddata = senddata
        # 请求地址
        self.url = "http://192.168.8.21/service"
        # 请求参数
        self.publicdata = {"buildVersion": "100",
                           "device": "phpService",
                           "partnerId": "20170315123001000001",
                           "protocol": "httpPost",
                           # "service": "o2oQuerySysMessagePageList",
                           "signType": "MD5",
                           "systemVersion": "7.1",
                           "version": "1.0",
                           "appName":"o2o_user_wx_app",
                           "deviceId":"test111",
                           "system":"python3",
                           "orderNo":str(uuid.uuid4()),
                           "publicKey":"51face7d5d52497016e7865c052ac051"
                           }
        self.publicdata["service"] = self.service
        # 添加私有参数
        for k, v in self.senddata.items():
            self.publicdata[k] = v
        # 生成sign
        self.sign = buApiBase().getSign(buApiBase().data2strforilife(self.publicdata))
        self.publicdata["sign"] = self.sign
        del self.publicdata["publicKey"]

    def send2ilife(self):
        print("请求参数：%s" % self.publicdata)
        self.befortime = time.time()
        self.req = requests.post(self.url, self.publicdata)
        self.aftertime = time.time()
        self.reqtime = str(round((self.aftertime - self.befortime) * 1000, 3))
        return self.req.status_code, self.reqtime, self.req.text

if __name__ == "__main__":
    service = "/ilife/mobile/visitorDrawAward"
    senddata = {
                "userPhone":"18716201367",
                "merchantId":"SH00000003",
                "orderSn":"111803000000108309",
                }
    requs = request2ilifeApi(service, senddata).send2ilife()
    print(requs)
