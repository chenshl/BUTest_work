# coding:utf-8
# @author : csl
# @date   : 2018/06/15 09:55
# 测试主页

from flask import Flask, render_template, request
from web.flask_base.flask_object import app
from common.request2buApi import request2buApi

@app.route("/home", methods=["GET", "POST"])
def gethome():
    return render_template("home.html")

@app.route("/FlaskTutorial", methods=["GET", "POST"])
def succes():
    if request.method == "POST":
        reqserver = request.form["requestserver"]
        reqdata = request.form["requestdata"]
        req = request2buApi(reqserver, eval(reqdata)).send()  #json格式字符串转换为字典
        return render_template("postsuccess.html", resultdata=req)
    else:
        return render_template("404.html")