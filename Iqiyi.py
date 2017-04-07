# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

class Iqiyi(Bangumi):
    link = "http://www.iqiyi.com/dongman/bangumi.html"
    name = u"爱奇艺"

    def getBangumi(self):
        """Youku processing function"""
        # Get Iqiyi bangumi HTML
        req = urllib2.Request(self.link)
        res = urllib2.urlopen(req)
        html = res.read()
        # Give the HTML to BeautifulSoup
        # TODO: Change the parser to lxml for better performance
        soup = BeautifulSoup(html, "html.parser")
        bweek = soup.find(id='widget-qycpweekly')
        # Get the list of the week
        for child in bweek.children:
            if child.name == None:
                continue
            wd = int(child['data-day']) + 1
            binfos = child.find_all('h4')
            for binfo in binfos:
                bname, bsep, bupdate = binfo.string.partition(u'：')
                blink = binfo.parent.parent['href']
                self.add(wd, bname, bupdate, blink)
