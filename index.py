# # -*- coding:utf_8 -*-
import web
import os
from Bangumi import Bangumi
from Bilibili import getBilibili
from Youku import getYouku
from Iqiyi import getIqiyi
from PPTV import getPPTV
from AcFun import getAcfun

urls = (
    '/', 'Index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class Index:
    def GET(self):
        i = web.input()
        blists = []
        blists.append(getBilibili().generateHTMLTable())
        blists.append(getYouku().generateHTMLTable())
        blists.append(getIqiyi().generateHTMLTable())
        blists.append(getPPTV().generateHTMLTable())
        blists.append(getAcfun().generateHTMLTable())
        return render.index(blists)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
