# -*- coding:utf_8 -*-
from Bangumi import Bangumi
from Bilibili import getBilibili
from Youku import getYouku
from Iqiyi import getIqiyi
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

# Title lol
print '*************************************'.decode('utf-8').encode(type).center(80)
print '* Whoami 的中国视频网站动画番剧列表 *'.decode('utf-8').encode(type).center(80)
print '*              命令行版             *'.decode('utf-8').encode(type).center(80)
print '*************************************'.decode('utf-8').encode(type).center(80)

# Main process
errorCount = 0
errorCount += getBilibili().cmdPrint()
errorCount += getYouku().cmdPrint()
errorCount += getIqiyi().cmdPrint()

# End statistics
print '\n出错的网站数量：{}'.format(errorCount).decode('utf-8').encode(type)
print ''
