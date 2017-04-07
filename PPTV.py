# -*- coding:utf_8 -*-
import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

class PPTV(Bangumi):
    link = "http://cartoon.pptv.com/"
    name = u'PPTV'

    def getBangumi(self):
        """PPTV processing function"""
        # Get PPTV bangumi HTML
        req = urllib2.Request(self.link)
        res = urllib2.urlopen(req)
        html = res.read()
        # Give the HTML to BeautifulSoup
        # TODO: Change the parser to lxml for better performance
        soup = BeautifulSoup(html, "html.parser")
        # Get a list of a week
        blist = soup.find(id="ui-tabcont-2698017")
        wd = 0
        for bday in blist.children:
            # Remove None child
            if bday.name == None:
                continue
            binfolist = bday.find_all("dl")
            for binfo in binfolist:
                binfodd = binfo.find_all("dd")
                try:
                    bupdate = binfodd[2].string
                except IndexError:
                    bupdate = ''
                bname = binfodd[0].find('a').string
                blink = binfodd[0].find('a')['href']
                self.add(wd, bname, bupdate, blink)
            wd += 1
