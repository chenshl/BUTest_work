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
        self.url = "http://192.168.8.18:6880"  # 新自测环境
        # self.url = "http://192.168.8.35:6880"  # 新集成环境
        # self.url = "http://tubc.jinvovo.com"  # 新集成环境
        # self.url = "http://192.168.8.41:6880/tasker"  # 新集成环境
        # self.url = "http://192.168.2.54:9999"  # 远江本机


        # 公共参数
        self.pubdata = {
                        # "terraceId":"*******************************",  # i生活
                        # "terraceId":"*******************************",  # 币航
                        "terraceId": "*******************************",  # 长青
                        # "secret":"*******************************",  # i生活
                        # "secret":"*******************************",  # 币航
                        "secret": "*******************************",  # 长青
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


