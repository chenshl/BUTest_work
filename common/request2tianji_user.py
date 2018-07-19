# coding:utf-8
# @author : csl
# @date   : 2018/05/21 14:21
# 获取单个用户在线时长

import copy
import hashlib
import requests
from common.operateExcel import operateExcel
from common.writelog import writelog
import time

url = "https://tongji.jwwblockchain.com/openreport/api/visit_length"
data = {"open_user":"jvvtjdev",
        "site_id":"3",
        "date":"2018-07-11"
        }
# open_user = "20170929001000334474"  #金窝窝用户ID单个用户获取
auth_token = "58bf9b67ba51f20f677c183302c72a3d"

# 参数拼接
def data2str():
    params = copy.deepcopy(data)  #深度拷贝data
    paramslist = sorted(params.items()) #按照params的key值排序
    datastr = ""
    for i in  paramslist:
        datastr += i[0] + "=" + i[1] + "&"
    # return datastr.rstrip("&")  #删除末尾"&"
    return datastr

# 签名串
def getSign():
    pubparam = data2str()
    paramsignstr = pubparam + "token_auth" + "=" + auth_token
    m = hashlib.md5()  # 生成一个md5 hash对象
    m.update(paramsignstr.encode('utf-8'))  # 生成hash对象后，用update方法对字符串进行md5加密的更新处理
    md5str = m.hexdigest().upper()  # 16进制的加密结果字符串,转大写
    return md5str



# 单个用户
open_user = "171c8422-934f-11e5-80e3-d89d672713e0"  #金窝窝用户ID单个用户获取
# 完整地址
requrl = url + "/"+ open_user + "?" + data2str() + "sign" + "=" + getSign()
print(requrl)
req = requests.get(requrl)
print(req.status_code)
print(req.text)



# # 多个用户
# userID = operateExcel().read_07_Excel("../datas/userID.xlsx", "Sheet1")
# write_path = "../datas/result.xlsx"
# resultdatas = []
#
# for x in range(0,20):
#     for user in userID:
#         requrl = url + "/"+ user + "?" + data2str() + "sign" + "=" + getSign()
#         print(requrl)
#         try:
#             beforetime = time.time()
#             req = requests.get(requrl)
#             aftertime = time.time()
#             writelog("info", "耗时：%s ms -- 查询用户ID：%s -- 返回结果：%s" % (str((aftertime - beforetime) * 1000), user, req.text))
#             resultdata = [str(time.strftime('%Y-%m-%d %H:%M:%S')),str((aftertime - beforetime) * 1000), str(user), str(req.text)]
#             resultdatas.append(resultdata)
#             # operateExcel().write_07_Excel(write_path, resultdata)
#             print(req.status_code)
#             print(req.text)
#         except Exception as e:
#             writelog("error", str(e))
#         continue
#
# operateExcel().write_07_Excel(write_path, resultdatas)
# print("测试结束。。。")

