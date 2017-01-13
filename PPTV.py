# -*- coding:utf_8 -*-
import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

PPTVURL = "http://cartoon.pptv.com/"

def getPPTV():
    """PPTV processing function"""
    # Get PPTV bangumi HTML
    req = urllib2.Request(PPTVURL)
    try:
        res = urllib2.urlopen(req)
        html = res.read()
    except urllib2.URLError:
        return Bangumi.empty('PPTV')
    bangumi = Bangumi('PPTV')
    # Give the HTML to BeautifulSoup
    # TODO: Change the parser to lxml for better performance
    soup = BeautifulSoup(html, "html.parser")
    # Get a list of a week
    blist = soup.find(id="ui-tabcont-2709445")
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
            bangumi.add(wd, bname, bupdate)
        wd += 1
    return bangumi
    
    

