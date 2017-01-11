# -*- coding:utf_8 -*-
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

class Bangumi:
    """A class for the bangumi in a website"""
    bangumi = {'Sunday': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': []}
    name = 'Nothing'

    def __init__(self, name):
        self.name = name

    # Create an empty Bangumi class.
    @staticmethod
    def empty(name):
        b = Bangumi(name)
        for key in b.bangumi.keys():
            b.bangumi[key].append(('读取失败', 'TAT'))
        return b

    # Print out the Bangumi class
    def cmdPrint(self):
        print '--------------------------------------------------------------------------------'
        print '                        ', self.name.decode('utf-8').encode(type)
        print '--------------------------------------------------------------------------------'
