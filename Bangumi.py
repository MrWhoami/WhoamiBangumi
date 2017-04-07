# -*- coding:utf_8 -*-
import sys
import re
import urllib2

class Bangumi:
    """A class for the bangumi in a website"""
    name = u'Nothing'
    link = 'http://'

    def __init__(self):
        self.bangumi = [[], [], [], [], [], [], []]
        self.errorFlag = True
        try:
            self.getBangumi()
            self.errorFlag = False
        except urllib2.URLError:
            self.name += u' - URL Error'
        except (AttributeError, KeyError):
            self.name += u' - Analysis Error'
        except:
            self.name += u' - Unknown Error'
            print "Unexpected error:", sys.exc_info()[0]


    def getBangumi(self):
        """A method for child to implement"""
        pass

    def add(self, dayOfWeek, name, update, link=None):
        """Add a new bangumi into the set"""
        dow = dayOfWeek % 7
        if link == None:
            link = self.link
        self.bangumi[dow].append((name, update, link))

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
