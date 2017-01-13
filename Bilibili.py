# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

BilibiliURL = "http://bangumi.bilibili.com/anime/timeline"

def decodeWeekday(wds):
    """Decode Unicode weekday into number"""
    if wds == '周一'.decode('utf-8'):
        return 1
    elif wds == '周二'.decode('utf-8'):
        return 2
    elif wds == '周三'.decode('utf-8'):
        return 3
    elif wds == '周四'.decode('utf-8'):
        return 4
    elif wds == '周五'.decode('utf-8'):
        return 5
    elif wds == '周六'.decode('utf-8'):
        return 6
    else:
        return 0

def getBilibili():
    """bilibili.tv processing function"""
    # Get bilibili bangumi HTML
    req = urllib2.Request(BilibiliURL)
    try:
        res = urllib2.urlopen(req)
        html = res.read()
    except URLError:
        return Bangumi.empty('bilibili')
    bangumi = Bangumi('bilibili')
    # Give the HTML to BeautifulSoup
    # TODO: Change the parser to lxml for better performance
    soup = BeautifulSoup(html, "html.parser")
    # Get a list of a week
    ul = soup.find(id="bangumi")
    count = 0
    for child in ul.children:
        # Remove None child
        if child.name == None:
            continue
        # Bilibili has two more week days....
        count += 1
        if count > 7:
            break
        # Get the week day
        wdS = child.find(attrs={"class":"week-day"}).string
        wd = decodeWeekday(wdS)
        # the list of a day
        blist = child.find(attrs={"class":"bangumi c-list"})
        for b in blist.children:
            if b.name == None:
                continue
            binfo = b.find(attrs={"class":"r-i"})
            bname = binfo.find('span').string.encode('utf-8')
            bupdate = binfo.find(attrs={"class":"update-info"}).string.encode('utf-8')
            bangumi.add(wd, bname, bupdate)
    return bangumi
    
    
