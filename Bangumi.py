# -*- coding:utf_8 -*-
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

class Bangumi:
    """A class for the bangumi in a website"""
    bangumi = [([], u'周日'),
               ([], u'周一'),
               ([], u'周二'),
               ([], u'周三'),
               ([], u'周四'),
               ([], u'周五'),
               ([], u'周六')]
    name = u'Nothing'
    errorFlag = False

    def __init__(self, name):
        self.name = name
        self.bangumi = [([], u'周日'),
                        ([], u'周一'),
                        ([], u'周二'),
                        ([], u'周三'),
                        ([], u'周四'),
                        ([], u'周五'),
                        ([], u'周六')]
        self.errorFlag = False

    @staticmethod
    def empty(name):
        """Create an empty Bangumi class."""
        b = Bangumi(name)
        b.errorFlag = True
        return b

    def add(self, dayOfWeek, name, episode):
        """Add a new bangumi into the set"""
        dow = dayOfWeek % 7
        self.bangumi[dow][0].append((name, episode))

    def cmdPrint(self):
        """Print out the Bangumi class"""
        if self.errorFlag:
            print (self.name + u' 出错啦 QAQ').encode(type)
            return 1
        print '--------------------------------------------------------------------------------'
        print self.name.encode(type).center(80)
        print '--------------------------------------------------------------------------------'
        for i in self.bangumi:
            print '===== {0} ====='.format(i[1].encode(type)).center(80)
            for j in i[0]:
                print j[0].encode(type).rjust(38), ' -- ', j[1].encode(type)
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
            blists.append(b[0])
            if len(b[0]) > listlen:
                listlen = len(b[0])
        for blist in blists:
            indent = listlen - len(blist)
            for i in range(indent):
                blist.append((' ', ' '))
        # Generate the table body
        for i in range(listlen):
            output += '<tr>'
            for j in range(7):
                output += '<td>{0}<br><em>{1}</em></td>'.format(blists[j][i][0].encode('utf-8'), blists[j][i][1].encode('utf-8'))
            output += '</tr>'
        # Generate the table footer
        output += '</table>'
        return output
