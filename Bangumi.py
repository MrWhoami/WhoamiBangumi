# -*- coding:utf_8 -*-
import sys
import re

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
