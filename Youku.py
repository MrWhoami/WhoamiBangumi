# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

class Youku(Bangumi):
    link = "http://comic.youku.com"
    name = u'优酷'

    def getBangumi(self):
        """Youku processing function"""
        # Get Youku bangumi HTML
        req = urllib2.Request(self.link)
        res = urllib2.urlopen(req)
        html = res.read()
        # Give the HTML to BeautifulSoup
        # TODO: Change the parser to lxml for better performance
        soup = BeautifulSoup(html, "html.parser")
        # Get the list by day of the week
        for wd in range(7):
            if wd == 0:
                lid = "tab_100895_7"
            else:
                lid = "tab_100895_{}".format(wd)
            div = soup.find(id=lid)
            blist = div.find_all("div", class_="v-meta va")
            for binfo in blist:
                bupdate = binfo.find("span", class_="v-status").string
                btitle = binfo.find(class_="v-meta-title")
                bname = btitle.find("a").string
                blink = btitle.find('a')['href']
                self.add(wd, bname, bupdate, blink)
