# -*- coding:utf_8 -*-

def dow2string(dow):
    '''Day of week number to string'''
    weekString = [u'周日', u'周一', u'周二', u'周三',
                  u'周四', u'周五', u'周六']
    return weekString[dow % 7]
