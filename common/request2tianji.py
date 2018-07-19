# coding:utf-8
# @author : csl
# @date   : 2018/05/18 17:20
# 访问天玑在线时长，请求方式get
import copy
import hashlib
import requests

url = "https://tongji.jwwblockchain.com/openreport/api/visit_length"
auth_token = "58bf9b67ba51f20f677c183302c72a3d"

data = {"open_user":"jvvtjdev",
        "site_id":"3",
        "date":"2018-05-18",
        "filter_visit_length":"40",
        "filter_visit_length_op":"gt"}

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

# 完整地址
requrl = url + "?" + data2str() + "sign" + "=" + getSign()

if __name__ == "__main__":
    # print(data2str())
    # print(getSign())
    print(requrl)
    req = requests.get(requrl)
    print(req.status_code)
    print(req.text)