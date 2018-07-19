# coding:utf-8
# @author : csl
# @date   : 2018/06/01 11:30
# BU1.0内嵌版查询类接口自动化测试脚本

import unittest
from common.request2buApi import request2buApi
from common.base import buApiBase

class BU_wallet_v1(unittest.TestCase):
    """BU钱包内嵌版"""
    def setUp(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjgxMDUzMDUsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjE4NzE2MjAwMDA2In0.nhHKKogbLT6lm2tv5uulkGsMTJ0f4htC83S1Rzb3glU"
        # 正式token
        # self.token = "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mjg5NjYxNjQsInN1YiI6IndhbGxldOezu-e7nyIsInBhcnRuZXJJZCI6ImNhZWIyZjEzN2RkNTgxYmY4ZjExYTNhMmJjMTkwYjU4IiwidXNlck1vYmlsZSI6IjE4NzE2MjAxMzY3In0.trTBXy86otWK64OQCgTqZXmXPzDEkLrqkJ6DOmeEHpQ"
    def tearDown(self):

        pass

    def test_verifyToken(self):
        """验证token"""
        self.service = "/wallet/v1/verifyToken"
        self.secdata = {"token":self.token}
        r = request2buApi(self.service, self.secdata).send()

    def test_myAssert(self):
        """查询我的资产"""
        self.service = "/wallet/v1/myAssert"
        self.secdata = {"token":self.token}
        r = request2buApi(self.service, self.secdata).send()

    def test_worldRank(self):
        """BU世界排行榜"""
        self.service = "/wallet/v1/worldRank"
        self.secdata = {"page":"2",
                        "pageSize":"10"}
        r = request2buApi(self.service, self.secdata).send()

    def test_qRCodeParam(self):
        """获取二维码参数"""
        self.service = "/wallet/v1/qRCodeParam"
        self.secdata = {"token":self.token}
        r = request2buApi(self.service, self.secdata).send()

    def test_assertFlow(self):
        """BU流水查询"""
        self.service = "/wallet/v1/assertFlow"
        self.tdtime = "2018-07-22 10:22:22"
        self.dtime = buApiBase().time2Timestamps(self.tdtime)  # 指定时间转换为毫秒时间戳
        # self.dtime = buApiBase().nowtime2Timestamps()
        self.secdata = {"token": self.token,
                        "flag": "0",
                        "dateFlag": "0",
                        "unixTimestamp": self.dtime,
                        "page": "1",
                        "pageSize": "40"}
        r = request2buApi(self.service, self.secdata).send()
        # self.assertRegexpMatches(r[1], "buValue", msg="请求断言失败")  # 验证正则表达式regexp搜索匹配的文本text

    def test_userCurMonthIncome(self):
        """本月收入和全球榜xx%"""
        self.service = "/wallet/v1/userCurMonthIncome"
        self.secdata = {"token":self.token}
        r = request2buApi(self.service, self.secdata).send()

    def test_userHalfYearIncome(self):
        """近半年收益"""
        self.service = "/wallet/v1/userHalfYearIncome"
        self.secdata = {"token":self.token}
        r = request2buApi(self.service, self.secdata).send()

    def test_customerSignData(self):
        """签到热门任务"""
        self.service = "/wallet/v1/customerSignData"
        self.secdata = {"token":self.token,
                        "pageSize":"20"}
        r = request2buApi(self.service, self.secdata).send()

    def test_taskList(self):
        """任务列表"""
        self.service = "/wallet/v1/taskList"
        self.secdata = {"token":self.token,
                        "page":"1",
                        "pageSize":"8"}
        r = request2buApi(self.service, self.secdata).send()

    def test_taskInfo(self):
        """任务详情"""
        self.service = "/wallet/v1/taskInfo"
        self.secdata = {"token":self.token,
                        "behaviorId":"0001A001B004"}
        r = request2buApi(self.service, self.secdata).send()

    def test_selectServe(self):
        """合作平台商品查询"""
        self.service = "/wallet/v1/selectServe"
        self.secdata = {"page":"1",
                        "pageSize":"10"}
        r = request2buApi(self.service, self.secdata).send()

if __name__ == "__main__":
    unittest.main()
