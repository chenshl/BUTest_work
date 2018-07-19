#!/usr/bin/python3
# coding:utf-8
# @author : csl
# @date   : 2018/06/15 10:46
# flask启动封装

from web.flask_base.flask_object import app

app.run(host="0.0.0.0", port=9001, debug=True)