# coding:utf-8
# @author : csl
# @date   : 2018/05/28 11:35
# BU钱包内嵌版接口单个调试

from common.request2buApi import request2buApi
from common.base import buApiBase

token = "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mjk1NDU4MzMsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjE4NzE2MjAwMDAyIn0.BiVziyb6Wf7LWLZsy6mS0DwHl24IavwEmvOV7p7gbJw"
# service = "/wallet/v1/sendValidateMsgCode"  # 授权短信不返回值，数据库或手机端查看短信验证码
# secdata = {"userMobile": "18716200007"}

# service = "/wallet/v1/authorize"  #授权
# secdata = {"userMobile": "18716200007",
#            "partnerId":"caeb2f137dd581bf8f11a3a2bc190b58",
#            "validateCode":"695661"}

# service = "/wallet/v1/verifyToken"  # 验证token
# secdata = {"token": token}

# service = "/wallet/v1/myAssert"  # 查询我的资产
# secdata = {"token":token}

# service = "/wallet/v1/worldRank"  # BU 世界排行榜
# secdata = {"page":"4",
#            "pageSize":"20"}

# service = "/wallet/v1/qRCodeParam"  # 获取二维码参数
# secdata = {"token":token}

# service = "/wallet/v1/setPassword"  # 交易密码设置
# secdata = {"token":token,
#            "password":"111111"}

# service = "/wallet/v1/assertFlow"  # BU流水查询
# tdtime = "2018-06-08 10:22:22"
# dtime = buApiBase().time2Timestamps(tdtime)  #指定时间转换为毫秒时间戳
# # dtime = buApiBase().nowtime2Timestamps()
# secdata = {"token":token,
#            "flag":"0",
#            "dateFlag":"0",
#            "unixTimestamp":dtime,
#            "page":"1",
#            "pageSize":"40"}

# service = "/wallet/v1/userCurMonthIncome"  # 本月收入和全球榜xx%
# secdata = {"token":token}

# service = "/wallet/v1/userHalfYearIncome"  # 近半年收益
# secdata = {"token":token}

# service = "/wallet/v1/customerSignData"  # 签到热门任务
# secdata = {"token":token,
#            "pageSize":"20"}

# service = "/wallet/v1/doSign"  # 签到动作
# secdata = {"token":token}

# service = "/wallet/v1/taskList"  # 任务列表
# secdata = {"token":token,
#            "page":"1",
#            "pageSize":"8"}

# service = "/wallet/v1/taskInfo"  # 任务详情
# secdata = {"token":token,
#            "behaviorId":"0001A001B009"}

# service = "/wallet/v1/selectServe"  # 合作平台商品查询
# secdata = {"page":"1",
#            "pageSize":"10"}

# service = "/wallet/v1/insertServe"  # 合作平台商品创建
# secdata = {"partnerId":"caeb2f137dd581bf8f11a3a2bc190b58",
#            "siteId":"ps003",
#            "serveImage":"www.baidu.com",
#            "serveInfo":"你妹你妹你妹妹",
#            "serveBu":"10",
#            "serveOriginalBu":"20",
#            "serveUrl":"www.baidu.com",
#            "categoryCode":"w303",
#            "serveShow":"1",
#            "serveSort":"1",
#            "serveBtn":"换",
#            "serveTitle":"换购换购",
#            "serveType":"2"}

# service = "/wallet/v1/updateServe"  # 合作平台商品修改
# secdata = {"partnerId":"66113584fa24a78f86f2e4741dae28d5",
#            "siteId":"ps001",
#            "serveImage":"www.baidu.com",
#            "serveInfo":"你妹你妹你妹妹aaaaaa",
#            "serveBu":"10",
#            "serveOriginalBu":"20",
#            "serveUrl":"www.baidu.com",
#            "categoryCode":"w303",
#            "serveShow":"1",
#            "serveSort":"1",
#            "serveBtn":"换",
#            "serveTitle":"换购换购",
#            "serveType":"2",
#            "serveId":"9"}
# secdata = {"serveImage":"www.xinlang.com",
#            "serveInfo":"bbbb你妹你妹你妹妹aaaaaa",
#            "serveId":"9",
#            "serveType": "2"}

# service = "/wallet/v1/pullMyBu"  # 领取BU动作
# secdata = {"token":token,
#            "behaviorId":"0001A001B002"}

# service = "/wallet/v1/createAssert"  # BU单个发放
# secdata = {"token":token,
#            "behaviorId":"0001A001B013",
#            "orderNum":"ceshi00101",
#            "money":"10000"
#            }

# # 重置钱包Redis缓存数据（避免每次重启）
# service = "/wallet/v1/resetCache"
# secdata = {"key":"WALLET_WORLD_RANK","partnerId":"caeb2f137dd581bf8f11a3a2bc190b58"}  #资产排行榜
# secdata = {"key":"WALLET_USER_RANK_CURMONTH_INCOME","partnerId":"caeb2f137dd581bf8f11a3a2bc190b58"}  #用户当月收入和击败榜
# secdata = {"key":"WALLET_PARTNER_ACCOUNT_LINK","partnerId":"caeb2f137dd581bf8f11a3a2bc190b58"}  #用户平台关系

r = request2buApi(service, secdata).send()
print(r)
