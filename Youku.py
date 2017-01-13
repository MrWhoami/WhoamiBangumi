# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

YoukuURL = "http://comic.youku.com"

def getYouku():
    """Youku processing function"""
    # Get Youku bangumi HTML
    req = urllib2.Request(YoukuURL)
    try:
        res = urllib2.urlopen(req)
        html = res.read()
    except URLError:
        return Bangumi.empty(u'优酷')
    bangumi = Bangumi(u'优酷')
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
        blist = div.find_all("div", attrs={"class": "v-meta va"})
        for binfo in blist:
            bupdate = binfo.find("span", attrs={"class": "v-status"}).string
            btitle = binfo.find(attrs={"class": "v-meta-title"})
            bname = btitle.find("a").string
            bangumi.add(wd, bname, bupdate)
    return bangumi
    
    
