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
