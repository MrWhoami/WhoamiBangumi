# -*- coding:utf_8 -*-
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
        i = web.input(keyword=None)
        bilibili = getBilibili()
        acfun = getAcfun()
        pptv = getPPTV()
        iqiyi = getIqiyi()
        youku = getYouku()
        blists = []
        blists.append(acfun.generateHTMLTable())
        blists.append(bilibili.generateHTMLTable())
        blists.append(iqiyi.generateHTMLTable())
        blists.append(pptv.generateHTMLTable())
        blists.append(youku.generateHTMLTable())
        searchResult = None
        if i.keyword:
            searchResult = []
            searchResult.extend(acfun.getSearch(i.keyword))
            searchResult.extend(bilibili.getSearch(i.keyword))
            searchResult.extend(iqiyi.getSearch(i.keyword))
            searchResult.extend(pptv.getSearch(i.keyword))
            searchResult.extend(youku.getSearch(i.keyword))
        return render.index(blists, searchResult)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
