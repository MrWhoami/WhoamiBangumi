# -*- coding:utf_8 -*-
import web
import os
from datetime import datetime, timedelta
from Bangumi import Bangumi
import Bilibili, Youku, Iqiyi, PPTV, AcFun
import Tools

if os.path.basename(__file__) == 'index.wsgi':
    import sae

urls = (
    '/', 'Index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class Index:
    def __init__(self):
        self.refreshData()
        self.dataTimeLimit = 15 * 60

    def refreshData(self):
        self.bilibili = Bilibili.getBilibili()
        self.acfun = AcFun.getAcfun()
        self.pptv = PPTV.getPPTV()
        self.iqiyi = Iqiyi.getIqiyi()
        self.youku = Youku.getYouku()
        self.refreshTime = datetime.now()

    def generateHTMLTable(self, bo):
        """Generate a html format table"""
        if bo.errorFlag:
            return '<p><b>{0} 访问失败</b></p>'.format(bo.name.encode('utf-8'))
        # Generate the table header
        output = '<hr /><h2>{0}</h2>'.format(bo.name.encode('utf-8'))
        output += '<table border="1">'
        output += '<tr><th>星期日</th><th>星期一</th><th>星期二</th><th>星期三</th>'
        output += '<th>星期四</th><th>星期五</th><th>星期六</th></tr>'
        # Prepare the table
        blists = []
        listlen = 0
        for b in bo.bangumi:
            blists.append(b)
            if len(b) > listlen:
                listlen = len(b)
        for blist in blists:
            indent = listlen - len(blist)
            for i in range(indent):
                blist.append(('', ' ', ''))
        # Generate the table body
        for i in range(listlen):
            output += '<tr>'
            for j in range(7):
                output += '<td><a href="{blink}">{bname}</a><br><em>{bupdate}</em></td>'.format(
                    bname=blists[j][i][0].encode('utf-8'),
                    bupdate=blists[j][i][1].encode('utf-8'),
                    blink=blists[j][i][2].encode('utf-8'))
            output += '</tr>'
        # Generate the table footer
        output += '</table>'
        return output

    def getSearch(self, keywords_s, bo):
        keywords = keywords_s.split()
        results = bo.search(keywords)
        resStrs = []
        for result in results:
            resStr = '<a href="{blink}">{bname} - {bsrc} - {bdow} - {bupdate}</a>'.format(
                bdow    = Tools.dow2string(result[0]).encode('utf-8'),
                bname   = result[1].encode('utf-8'),
                bupdate = result[2].encode('utf-8'),
                blink   = result[3].encode('utf-8'),
                bsrc    = bo.name.encode('utf-8'))
            resStrs.append(resStr)
        return resStrs

    def GET(self):
        i = web.input(keyword=None)
        now = datetime.now()
        if (now - self.refreshTime).total_seconds > self.dataTimeLimit:
            self.refreshData()
        blists = []
        blists.append(self.generateHTMLTable(self.acfun))
        blists.append(self.generateHTMLTable(self.bilibili))
        blists.append(self.generateHTMLTable(self.iqiyi))
        blists.append(self.generateHTMLTable(self.pptv))
        blists.append(self.generateHTMLTable(self.youku))
        searchResult = []
        if i.keyword:
            searchResult.extend(self.getSearch(i.keyword, self.acfun))
            searchResult.extend(self.getSearch(i.keyword, self.bilibili))
            searchResult.extend(self.getSearch(i.keyword, self.iqiyi))
            searchResult.extend(self.getSearch(i.keyword, self.pptv))
            searchResult.extend(self.getSearch(i.keyword, self.youku))
        return render.index(blists, searchResult)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

if os.path.basename(__file__) == 'index.wsgi':
    app = web.application(urls, globals()).wsgifunc()
    application = sae.create_wsgi_app(app)
