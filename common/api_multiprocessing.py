# coding:utf-8
# @author : csl
# @date   : 2018/06/25 15:19
# 多进程处理，进程参数不可在相互间使用，不作为并发测试代码使用，每个进程之间默认不能共用内存

import multiprocessing
from common.request2buApi import request2buApi
from common.operateExcel import operateExcel


class tomultiprocess(multiprocessing.Process):

    def __init__(self, processID, name, service, data, signal):
        multiprocessing.Process.__init__(self)
        self.processID = processID
        self.name = name
        self.service = service
        self.data = data
        self.signal = signal


    # 重写Process的run()
    def run(self):
        self.signal.wait()
        r = request2buApi(self.service, self.data).send()
        print([r[4], r[0], r[1], r[3], r[2]])


if __name__ == "__main__":
    processes = []
    butokens = operateExcel().read_07_Excel("../datas/BUtoken.xlsx", "Sheet1")
    service = "/wallet/v1/myAssert"  # 接口名称
    dfprocessID = 1
    event_signal = multiprocessing.Event()
    for i in range(1,2):
        for butoken in butokens:
            datatmp = {"token":butoken}  # 动态获取用户token参数
            processx = "process" + str(dfprocessID)
            processname = "process-" + str(dfprocessID)
            processx = tomultiprocess(dfprocessID, processname, service, datatmp, event_signal)
            processes.append(processx)
            dfprocessID += 1
    for processwt in processes:
        processwt.start()
    event_signal.set()
    for processon in processes:
        processon.join()
    print("退出主线程")