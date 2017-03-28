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
    except urllib2.URLError:
        return Bangumi.empty('bilibili', BilibiliURL)
    bangumi = Bangumi('bilibili', BilibiliURL)
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
        wdS = child.find(class_="week-day").string
        wd = decodeWeekday(wdS)
        # the list of a day
        blist = child.find(class_="bangumi c-list")
        for b in blist.children:
            if b.name == None:
                continue
            binfo = b.find(class_="r-i")
            if not binfo:
                break
            bname = binfo.find('span').string
            bupdate = binfo.find(class_="update-info").string
            blink = binfo.find('a')['href']
            bangumi.add(wd, bname, bupdate, blink)
    return bangumi
    
    
