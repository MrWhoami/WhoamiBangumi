# -*- coding:utf_8 -*-
import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

class AcFun(Bangumi):
    name = u'AcFun'
    link = "http://www.acfun.cn"
    def getBangumi(self):
        """AcFun processing function"""
        # Get AcFun bangumi HTML
        req = urllib2.Request(self.link)
        res = urllib2.urlopen(req)
        html = res.read()
        # Give the HTML to BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Get lists of a week
        bweek = soup.find_all(class_="time-block")
        wd = 1
        for binfoList in bweek:
            binfos = binfoList.find_all('li')
            for binfo in binfos:
                bname = binfo.find('b').string
                bupdate = binfo.find('p').string
                blink = self.link + binfo.find('b').parent['href']
                # Remove special character may cause GBK encoding error
                if '•'.decode('utf-8') in bupdate:
                    bupdate = bupdate[2:]
                self.add(wd, bname, bupdate, blink)
            wd += 1
