# coding:utf-8
# @author : csl
# @date   : 2018/07/02 17:01
# 天玑在线时长查询

from flask import Flask, render_template, request
from web.flask_base.flask_object import app
from common.request2tianji_user_class import request2tianji_user_class

@app.route("/onlinetimes", methods=["GET", "POST"])
def inquire_tianji_onlinetimes():
    return render_template("tianji_onlinetimes.html")

@app.route("/tianjireqresult", methods=["GET", "POST"])
def gettianjireqresult():
    if request.method == "POST":
        userType = request.form["userType"]
        budate = request.form["budate"]
        jinvovouserid = request.form["userid"]
        req = request2tianji_user_class(userType, budate, jinvovouserid).send2tianji()
        return render_template("postsuccess.html", resultdata=req)
    else:
        return render_template("404.html")



