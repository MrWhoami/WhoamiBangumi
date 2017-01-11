# -*- coding:utf_8 -*-
from Bangumi import Bangumi
import Bilibili
import sys

# For Chinese printing orz
type = sys.getfilesystemencoding()

# Title lol
print '*************************************'.decode('utf-8').encode(type)
print '* Whoami 的中国视频网站动画番剧列表 *'.decode('utf-8').encode(type)
print '*            命令行版               *'.decode('utf-8').encode(type)
print '*************************************'.decode('utf-8').encode(type)

# Main process
Bilibili.getBilibili().cmdPrint()
