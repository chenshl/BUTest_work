# coding:utf-8
# @author : csl
# @date   : 2018/06/15 10:18
# 创建Flask类应用对象,导入视图views

from flask import Flask

app = Flask(__name__, template_folder=r"..\templates")  #template_folder指定静态文件路径，默认为当前路径下的templates文件夹
# 先定义Flask对象后再导入views页面
from web.views import homePage
from web.views import tianji_online_timesPage