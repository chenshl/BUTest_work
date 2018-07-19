# coding:utf-8
# @author : csl
# @date   : 2018/06/04 11:24
# BU钱包接口多线程处理单独封装

import threading
from common.request2buApi import request2buApi
# from common.writelog import writelog
import time
from common.operateExcel import operateExcel
import random

global thred_reqresults  # 定义结果常量用于保存请求结果数据
thred_reqresults = []

class tothread(threading.Thread):

    def __init__(self, threadID, name, service, data, signal):

        # threadID  线程ID
        # name      线程名称
        # counter   线程个数
        # service   接口名称
        # data      接口参数
        # signal    线程等待标记

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.service = service
        self.data = data
        self.signal = signal

    # 重写Thread的run()
    def run(self):

        # writelog("info", "请求时间：%s   线程名称：%s  线程ID：%s" % (time.strftime('%Y-%m-%d %H:%M:%S'), self.name, self.threadID))
        self.signal.wait() # 线程等待请求
        r = request2buApi(self.service, self.data).send()
        global thred_reqresults
        thred_reqresults.append([r[4], r[0], r[1], r[3], r[2]])  # 保存返回结果



if __name__ == "__main__":

    # # 单个用户并发
    # # 创建线程对象
    # service = "/wallet/v1/worldRank"  # 接口名称
    # # secdata = {"token": "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjgzNzIyOTUsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjE4NzE2MjAxMzY3In0.dOHir3kY3e829BLlig-HmMcgXgyIPPn2vrUNokOK3CQ"}
    # secdata = {"page":"2","pageSize":"10"}
    # threads = []
    # for i in range(1,301):
    #     threadx = "thread"+str(i)
    #     threadname = "Thread-" + str(i)
    #     threadx = tothread(i, threadname, service, secdata)
    #     threads.append(threadx)
    #     # threadx.start()
    #     # threadx.join()  #主线程等待thread(x)线程结束才继续执行
    # # 启动所有线程
    # for threadwt in threads:
    #     threadwt.start()
    # # 主线程中等待所有子线程退出
    # for threadon in threads:
    #     threadon.join()
    # print("退出主线程。。。")



    # 多个用户并发
    threads = []
    movingdatas = operateExcel().read_07_Excel("../datas/BUphone.xlsx", "Sheet1")  # 获取Excel中的BUtoken
    service = "/app/v1/generalTran"   # 接口名称
    dfthreadID = 1
    event_obj = threading.Event()  # 定义flag线程等待，默认为false
    for i in range(0,5):
        for movingdata in movingdatas:
            # 动态获取用户参数
            datatmp = {"fromUserMobile":str(movingdata),
                       "toUserMobile":"18716200017",
                       "randomNum":"test_randomNum" + str(movingdata) + str(random.randint(1000,9999)),
                       "tranBody":"抽奖",
                       "outTradeNo":"test_outTradeNo_auto" + str(movingdata) + str(random.randint(1000,9999)) + str(random.randint(1000,9999)),
                       "createIp":"192.168.1.31",
                       "buAmount":"10",
                       # "attachStr":"teststr_001",  # 非必传
                       #  "notifyUrl":"192.168.1.31",  # 非必传
                       "startTime":"20180705094753"
                       }
            threadx = "thread" + str(dfthreadID)
            threadname = "Thread-" + str(dfthreadID)
            threadx = tothread(dfthreadID, threadname, service, datatmp, event_obj)
            threads.append(threadx)
            dfthreadID += 1
    print("开启线程进行等待。。。")
    for threadwt in threads:
        threadwt.start()
    print("等待中的线程数量：%s" % (threading.active_count()))
    event_obj.set()  # 重设线程标记为true，所有等待线程开始执行
    for threadon in threads:
        threadon.join()
    print("退出主线程")
    operateExcel().write_07_Excel("../datas/result.xlsx", thred_reqresults)  # 结果写入Excel
    # print(thred_reqresults)

