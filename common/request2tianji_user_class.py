# coding:utf-8
# @author : csl
# @date   : 2018/07/02 17:17
# 天玑在线时长查询封装类

import copy
import hashlib
import requests
# from common.operateExcel import operateExcel
from common.writelog import writelog
# import time

class request2tianji_user_class():

    def __init__(self, userType, budate, jinvovouserid):

        # userType  : 用户来源：3=长青，4=i生活
        self.url = "https://tongji.jwwblockchain.com/openreport/api/visit_length"
        self.data = {"open_user":"jvvtjdev",
                     "site_id":userType,
                     "date":budate
                     }
        self.auth_token = "58bf9b67ba51f20f677c183302c72a3d"
        self.open_user = jinvovouserid

    def data2str2(self):
        self.params = copy.deepcopy(self.data)  # 深度拷贝data
        self.paramslist = sorted(self.params.items())  # 按照params的key值排序
        self.datastr = ""
        for i in self.paramslist:
            self.datastr += i[0] + "=" + i[1] + "&"
        # return self.datastr.rstrip("&")  #删除末尾"&"
        return self.datastr

    def getSign2(seif):
        seif.pubparam = seif.data2str2()
        seif.paramsignstr = seif.pubparam + "token_auth" + "=" + seif.auth_token
        seif.m = hashlib.md5()  # 生成一个md5 hash对象
        seif.m.update(seif.paramsignstr.encode('utf-8'))  # 生成hash对象后，用update方法对字符串进行md5加密的更新处理
        seif.md5str = seif.m.hexdigest().upper()  # 16进制的加密结果字符串,转大写
        return seif.md5str

    def send2tianji(self):
        self.requrl = self.url + "/"+ self.open_user + "?" + self.data2str2() + "sign" + "=" + self.getSign2()
        self.req2tianji = requests.get(self.requrl)
        writelog("info", "请求地址--%s  返回数据--%s" % (self.requrl, str(self.req2tianji.text)))
        return self.req2tianji.status_code, self.req2tianji.text


if __name__ == "__main__":
    for i in range(1, 2):
        req = request2tianji_user_class("3", "2018-07-18", "20171018001000496719").send2tianji()
        print("第 %s 次请求结果：^%s" % (i, req))

