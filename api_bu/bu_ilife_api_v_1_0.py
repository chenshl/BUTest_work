# coding:utf-8
# @author : csl
# @date   : 2018/06/06 09:45
# BU平台接口单个调用

from common.request2buApi import request2buApi
from common.base import buApiBase

# service = "/ilife/v1/customerSignData"   #签到任务列表
# secdata = {"userMobile":"18716200010","categoryCode":"ilife001","pageSize":"40","page":"1"}
#
# service = "/ilife/v1/doSign"  #签到动作
# secdata = {"userMobile":"18716200010"}
#
# service = "/ilife/v1/taskList" #任务列表
# secdata = {"pageSize":"20",
#            "userMobile":"18716201367"}
#
# service = "/ilife/v1/taskInfo"  #任务详情
# secdata = {"behaviorId": "0001A001B009",
#            "userMobile":"18716201367"}
#
# service = "/ilife/v1/pullMyBu"  # 领取 BU 动作
# secdata = {"userMobile": "18716200008",
#            "behaviorId":"0001A001B002"}
#
# service = "/app/v1/partnerRecordBu"  #查询某平台 BU 赠送通知消息
# secdata = {"partnerIds": "caeb2f137dd581bf8f11a3a2bc190b58"}  #合作平台 id用 "," 分隔
#
# service = "/ilife/v1/worldRank"  #BU 世界排行榜
# secdata = {"page": "1",
#            "pageSize":"20"}
# secdata = {}
#
service = "/ilife/v1/myAssert"  #查询我的资产
secdata = {"userMobile": "18716201367"}
#
# service = "/ilife/v1/pullMyBu"  #领取BU动作
# secdata = {"userMobile": "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mjc0OTU1MDMsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjE4NzE2MjAwMDA4In0.mkJJ5FhyJDlPX-5tsWV92UaKT28eg_UAQSFMUWQfoTc",
#            "behaviorId":"0001A001B002"}

# service = "/ilife/v1/flowList"  #查询流水详情
# tdtime = "2018-07-04 10:22:22"
# dtime = buApiBase().time2Timestamps(tdtime)
# secdata = {"userMobile": "18716201367",
#            "flag":"0",
#            "dateFlag":"0",
#            "page":"1",
#            "unixTimestamp":dtime,  #当前时间戳，非必填
#            "showAll":"1",  #是否显示所有流水, 1=是，0=显示当前平台流水，默认=1,非必填
#            "pageSize":"20"}


r = request2buApi(service, secdata).send()
print(r)