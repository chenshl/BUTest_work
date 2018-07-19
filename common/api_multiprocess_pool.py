# coding:utf-8
# @author : csl
# @date   : 2018/06/26 11:16
# multiprocessing的Pool可以处理返回结果，但是进程并发时受processes设置限制

import multiprocessing
from common.request2buApi import request2buApi
from common.operateExcel import operateExcel

def do_req2bu(sever, data):
    r = request2buApi(sever, data).send()
    # print(r)
    return [r[4], r[0], r[1], r[3], r[2]]

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    server = "/wallet/v1/myAssert"
    datatmp = {"token": "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mjg0MTMxOTYsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjEzMDAxNDA5OTYyIn0.giMR91JI2-s52TBCFYfTMzWDcUILK2h-AydKOQBgTog"}
    poolresults = []
    poolreqresutls = []
    print("进程开始请求。。。")
    for i in range(2000):
        poolresults.append(pool.apply_async(do_req2bu, (server, datatmp)))
    pool.close()
    pool.join()
    print("请求结束，保存结果数据。。。")
    for result in poolresults:
        # print(result.get())
        poolreqresutls.append(result.get())
    operateExcel().write_07_Excel("../datas/result.xlsx", poolreqresutls)