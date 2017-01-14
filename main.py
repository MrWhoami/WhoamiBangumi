# -*- coding:utf_8 -*-
from Bangumi import Bangumi
from Bilibili import getBilibili
from Youku import getYouku
from Iqiyi import getIqiyi
from PPTV import getPPTV
from AcFun import getAcfun
from datetime import date
import sys

def printNotice():
    """Print notice info"""
    print u"""
注意 Notice：
    1. Bilibili 的番组在今天之前的两天显示的是正常的已经更新的内容，而今天之后标记的更新信息均为将要更新的内容，而不是已经更新的内容，今天则标记的是今天将要更新的内容，也可能是已经更新的，如：今天是周三，则周一、周二显示的是更新之后的内容，周四、周五、周六、周日显示的是即将更新的内容；
    2. 不显示更新信息的番剧可能是大长篇，也有可能是平台自制的节目；
    3. 今天是 {0}
    """.format(date.today().strftime('%A'))

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
errorCount += getAcfun().cmdPrint()

# End statistics
print u'\n出错的网站数量：{}'.format(errorCount).encode(type)
printNotice()
