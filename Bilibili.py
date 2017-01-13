# -*- coding:utf_8 -*-

import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

BilibiliURL = "http://bangumi.bilibili.com/anime/timeline"

def decodeWeekday(wds):
    """Decode Unicode weekday into number"""
    if wds == u'周一':
        return 1
    elif wds == u'周二':
        return 2
    elif wds == u'周三':
        return 3
    elif wds == u'周四':
        return 4
    elif wds == u'周五':
        return 5
    elif wds == u'周六':
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
            bname = binfo.find('span').string
            bupdate = binfo.find(attrs={"class":"update-info"}).string
            bangumi.add(wd, bname, bupdate)
    return bangumi
    
    
