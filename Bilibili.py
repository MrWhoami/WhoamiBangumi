# -*- coding:utf_8 -*-

import requests
from HTMLParser import HTMLParser
from Bangumi import Bangumi
 
class BilibiliParser(HTMLParser):
    """Parse the bilibili bangumi page and generate a bangumi object"""
    bangumi = Bangumi.empty('bilibili')

    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        pass

def getBilibili():
    """bilibili.tv processing function"""
    # Get bilibili bangumi HTML
    r = requests.post("http://bangumi.bilibili.com/anime/timeline")
    # Test if the HTML get successfully
    if r.status_code != requests.codes.ok:
        return Bangumi.empty('bilibili')
    # Give the HTML to Parser
    parser = BilibiliParser()
    parser.feed(r.text)
    return parser.bangumi
