# -*- coding:utf_8 -*-
from Bangumi import Bangumi
from Bilibili import getBilibili
from Youku import getYouku
from Iqiyi import getIqiyi
from PPTV import getPPTV
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

# Title lol
print u'*************************************'.encode(type).center(80)
print u'* Whoami 的中国视频网站动画番剧列表 *'.encode(type).center(80)
print u'*              命令行版             *'.encode(type).center(80)
print u'*************************************'.encode(type).center(80)

# Main process
errorCount = 0
errorCount += getBilibili().cmdPrint()
errorCount += getYouku().cmdPrint()
errorCount += getIqiyi().cmdPrint()
errorCount += getPPTV().cmdPrint()

# End statistics
print u'\n出错的网站数量：{}'.format(errorCount).encode(type)
print ''
