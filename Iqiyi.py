# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

IqiyiURL = "http://www.iqiyi.com/dongman/bangumi.html"

def getIqiyi():
    """Youku processing function"""
    # Get Iqiyi bangumi HTML
    req = urllib2.Request(IqiyiURL)
    try:
        res = urllib2.urlopen(req)
        html = res.read()
    except URLError:
        return Bangumi.empty('爱奇艺')
    bangumi = Bangumi('爱奇艺')
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
            bname, bsep, bupdate = binfo.string.partition('：'.decode('utf-8'))
            bangumi.add(wd, bname.encode('utf-8'), bupdate.encode('utf-8'))
    return bangumi
    
    
