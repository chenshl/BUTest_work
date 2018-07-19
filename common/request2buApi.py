# coding:utf-8
# @author : csl
# @date   : 2018/05/24 09:47
# 链接BU接口

from common.base import buApiBase
import requests
import copy
from common.writelog import writelog
import time

class request2buApi(object):

    def __init__(self, service, secdata):

        self.service = service
        # self.url = "http://192.168.8.21:6880/tasker"  # 内网开发环境
        # self.url = "https://ubc.jinvovo.com"   # 正式环境
        # self.url = "http://47.99.3.32"  # 新正式环境
        self.url = "http://192.168.8.18:6880"  # 新自测环境
        # self.url = "http://192.168.8.35:6880"  # 新集成环境
        # self.url = "http://tubc.jinvovo.com"  # 新集成环境
        # self.url = "http://192.168.8.41:6880/tasker"  # 新集成环境
        # self.url = "http://192.168.2.54:9999"  # 远江本机


        # 公共参数
        self.pubdata = {
                        # "terraceId":"caeb2f137dd581bf8f11a3a2bc190b58",  # i生活
                        # "terraceId":"5db0ca63904b8800c274a996bc8545ad",  # 币航
                        "terraceId": "6c7dbaa891b3f476b90be2b16c5cfdac",  # 长青
                        # "secret":"7413818815075981a28bb7733fa1387d",  # i生活
                        # "secret":"6b720eacdc49b2273a991ad1bf880e3a",  # 币航
                        "secret": "5106fca2bb5966141d93bb7b096d1418",  # 长青
                        "signType":"MD5",
                        "version":"v1.0",
                        "device":"ANDROID"
                        }
        # 添加私有参数
        for k,v in secdata.items():
            self.pubdata[k] = v

        self.datastr = buApiBase().data2str(self.pubdata)
        # print(self.datastr)
        self.cpdatastr = copy.deepcopy(self.pubdata)  #深度拷贝合并后的参数字典
        del self.cpdatastr["secret"]  #删除secret
        self.senddata = buApiBase().data2str(self.cpdatastr) + "&" + "sign" + "=" + buApiBase().getSign(self.datastr)
        # print(self.senddata)

    def send(self):
        self.geturl = self.url + self.service + "?" + self.senddata
        print(self.geturl)
        writelog("info", "请求地址--%s" % str(self.geturl))
        beforetime = time.time()
        req = requests.get(self.geturl)
        aftertime = time.time()
        reqtime = str(round((aftertime - beforetime) * 1000, 3))
        writelog("info", "请求耗用时长--%s ms  返回数据--%s" % (str(reqtime), str(req.text)))
        return reqtime, req.status_code, req.text, self.service, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(beforetime))


