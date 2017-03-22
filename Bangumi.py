# -*- coding:utf_8 -*-
import sys
import re

# For Chinese printing orz
charset = sys.getfilesystemencoding()

def dow2string(dow):
    '''Day of week number to string'''
    weekString = [u'周日', u'周一', u'周二', u'周三', 
                  u'周四', u'周五', u'周六']
    return weekString[dow % 7]

class Bangumi:
    """A class for the bangumi in a website"""
    bangumi = [[], [], [], [], [], [], []]
    name = u'Nothing'
    link = 'http://'
    errorFlag = False

    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.bangumi = [[], [], [], [], [], [], []]
        self.errorFlag = False

    @staticmethod
    def empty(name, link):
        """Create an empty Bangumi class."""
        b = Bangumi(name, link)
        b.errorFlag = True
        return b

    def add(self, dayOfWeek, name, update, link=None):
        """Add a new bangumi into the set"""
        dow = dayOfWeek % 7
        if link == None:
            link = self.link
        self.bangumi[dow].append((name, update, link))

    def cmdPrint(self):
        """Print out the Bangumi class"""
        if self.errorFlag:
            print (self.name + u' 出错啦 QAQ').encode(charset)
            return 1
        print '--------------------------------------------------------------------------------'
        print self.name.encode(charset).center(80)
        print '--------------------------------------------------------------------------------'
        for i in range(7):
            print '===== {0} ====='.format(dow2string(i).encode(charset)).center(80)
            for j in self.bangumi[i]:
                print j[0].encode(charset).rjust(38), ' -- ', j[1].encode(charset)
        return 0

    def generateHTMLTable(self):
        """Generate a html format table"""
        if self.errorFlag:
            return '<p><b>{0} 访问失败</b></p>'.format(self.name.encode('utf-8'))
        # Generate the table header
        output = '<hr /><h2>{0}</h2>'.format(self.name.encode('utf-8'))
        output += '<table border="1">'
        output += '<tr><th>星期日</th><th>星期一</th><th>星期二</th><th>星期三</th>'
        output += '<th>星期四</th><th>星期五</th><th>星期六</th></tr>'
        # Prepare the table
        blists = []
        listlen = 0
        for b in self.bangumi:
            blists.append(b)
            if len(b) > listlen:
                listlen = len(b)
        for blist in blists:
            indent = listlen - len(blist)
            for i in range(indent):
                blist.append(('', ' ', ''))
        # Generate the table body
        for i in range(listlen):
            output += '<tr>'
            for j in range(7):
                output += '<td><a href="{blink}">{bname}</a><br><em>{bupdate}</em></td>'.format(
                    bname=blists[j][i][0].encode('utf-8'),
                    bupdate=blists[j][i][1].encode('utf-8'),
                    blink=blists[j][i][2].encode('utf-8'))
            output += '</tr>'
        # Generate the table footer
        output += '</table>'
        return output

    def cmdSearch(self, en_keywords):
        '''Called by command line. Print the result to the console.'''
        keywords = []
        for keyword in en_keywords:
            keywords.append(keyword.decode(charset))
        result = self.search(keywords)
        if len(result) == 0:
            return 1
        else:
            print '===== {0} ====='.format(self.name.encode(charset)).center(80)
            for b in result:
                print (b[1] + ' - ' + b[2] + ' - ' + dow2string(b[0])).encode(charset)
            return 0
        

    def getSearch(self, keywords_s):
        keywords = keywords_s.split()
        results = self.search(keywords)
        resStrs = []
        for result in results:
            resStr = '<a href="{blink}">{bname} - {bsrc} - {bdow} - {bupdate}</a>'.format(
                    bdow    = dow2string(result[0]).encode('utf-8'),
                    bname   = result[1].encode('utf-8'),
                    bupdate = result[2].encode('utf-8'),
                    blink   = result[3].encode('utf-8'),
                    bsrc    = self.name.encode('utf-8'))
            resStrs.append(resStr)
        return resStrs

    def search(self, keywords):
        '''Inner search function. Need a list of keywords. Return a list of search result.'''
        resultList = []
        for dow in range(7):
            for b in self.bangumi[dow]:
                for keyword in keywords:
                    if keyword in b[0]:
                        resultList.append((dow, b[0], b[1], b[2]))
                        break
        return resultList
