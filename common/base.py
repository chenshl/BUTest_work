# coding:utf-8
# @author：csl
# @date  ：2018/05/24 09:22
# 基础方法
import copy
import hashlib
import time

class buApiBase(object):

    # 参数拼接
    def data2str(self, data):
        self.params = copy.deepcopy(data)  # 深度拷贝data
        self.paramslist = sorted(self.params.items())  # 按照params的key值排序
        self.datastr = ""
        for i in self.paramslist:
            self.datastr += i[0] + "=" + i[1] + "&"
        return self.datastr.rstrip("&")  #删除末尾"&"
        # return self.datastr

    # MD5签名串
    def getSign(self, str):
        self.paramsignstr = str
        m = hashlib.md5()  # 生成一个md5 hash对象
        m.update(self.paramsignstr.encode('utf-8'))  # 生成hash对象后，用update方法对字符串进行md5加密的更新处理
        self.md5str = m.hexdigest()  # 16进制的加密结果字符串
        return self.md5str

    # 指定时间转换为毫秒时间戳,返回str tdtime="2018-05-29 10:22:22"
    def time2Timestamps(self, tdtime):
        self.timeArray = time.strptime(tdtime, "%Y-%m-%d %H:%M:%S")
        self.stime = int(round(time.mktime(self.timeArray) * 1000))
        return str(self.stime)

    # 当前时间转换为毫秒时间戳，返回str
    def nowtime2Timestamps(self):
        self.stime = int(round(time.time() * 1000))
        return str(self.stime)

    # 参数拼接value值，i生活使用
    def data2strforilife(self, data):
        self.params = copy.deepcopy(data)
        self.paramslist = sorted(self.params.items())
        self.datastr = ""
        for i in self.paramslist:
            self.datastr += i[1]
        # print("加密前字符串：%s" % self.datastr[:-1])
        # return self.datastr[:-1]  # 去掉最后一位“&”
        return self.datastr