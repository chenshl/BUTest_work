# coding:utf-8
# @author : csl
# @date   : 2018/07/03 14:03
# BU系统迭代v2.0.2.5交易

from common.request2buApi import request2buApi
import random

# 创建单个资产
# service = "/app/createAssert"
# secdata = {"userMobile":"18716205001",
#            "behaviorId":"0002A001B006",
#            # "behaviorId":"0002N001B001",
#            "orderNum":"ceshi_orderNum_" + str(random.randint(1000,9999)) + str(random.randint(1000, 9999)),
#            "money":"10000"
#            }

# 合作平台内商户的注册
# service = "/app/v1/merchants"
# secdata = {"userMobile":"18716205001",
#            "userName":"陈圣林测试"
#            }

# BU转账
# service = "/app/v1/generalTran"
# secdata = {"fromUserMobile":"18716205000",
#            "toUserMobile":"18716205001",
#            "randomNum":"randomNum_" + str(random.randint(1000,9999)),
#            "tranBody":"test",
#            "outTradeNo":"outTradeNo_" + str(random.randint(1000,9999)) + str(random.randint(1000, 9999)),
#            "createIp":"192.168.1.31",
#            "buAmount":"100",
#            # "attachStr":"teststr_001",  # 非必传
#            # "notifyUrl":"192.168.1.31",  # 非必传
#            "startTime":"20180706094053"
#            }

# BU退货
service = "/app/v1/refundTran"
secdata = {"refundDesc":"一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十",
           "outRefundNo":"outTradeNo_18101113",
           "createIp":"192.168.1.31",
           "buAmount":"2.555",  #退款金额，如为空表示全部退款
           "randomNum":"BUtuihuo_" + str(random.randint(1000, 9999)),
           "outTradeNo":"BUtuihuo_" + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))
           }

req = request2buApi(service, secdata).send()
print(req)



# 批量创建BU账户用于测试
# service = "/app/createAssert"
# for i in range(2001, 4001):
#     usermobile = "1871620" + str(i)
#     secdata = {"userMobile":usermobile,
#                "behaviorId":"0002A001B006",
#                "orderNum":"autotest_" + str(random.randint(1000,9999)) + str(random.randint(1000, 9999)),
#                "money":"50000"
#                }
#     req = request2buApi(service, secdata).send()
#     print(req)
# print("数据创建完成")

