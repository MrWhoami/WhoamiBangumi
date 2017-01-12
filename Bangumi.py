# -*- coding:utf_8 -*-
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

class Bangumi:
    """A class for the bangumi in a website"""
    bangumi = [([], '周日'),
               ([], '周一'),
               ([], '周二'),
               ([], '周三'),
               ([], '周四'),
               ([], '周五'),
               ([], '周六')]
    name = 'Nothing'
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
            return self.name
        print '--------------------------------------------------------------------------------'
        print '                                 ', self.name.decode('utf-8').encode(type)
        print '--------------------------------------------------------------------------------'
        for i in self.bangumi:
            print '| {0} |'.format(i[1].decode('utf-8').encode(type))
            for j in i[0]:
                print j[0].decode('utf-8').encode(type) + ' - ' + j[1].decode('utf-8').encode(type)
