# -*- coding:utf_8 -*-
from datetime import date
import sys
from Bangumi import Bangumi
import Bilibili, Youku, Iqiyi, PPTV, AcFun
import Tools


class CLIApp:
    def __init__(self, keywords):
        self.errorCount = 0
        self.bilibili = Bilibili.getBangumi()
        self.acfun = AcFun.getBangumi()
        self.pptv = PPTV.getBangumi()
        self.iqiyi = Iqiyi.getBangumi()
        self.youku = Youku.getBangumi()
        self.en_keywords = keywords
        # For Chinese printing orz
        self.charset = sys.getfilesystemencoding()

    def printNotice(self):
        """Print notice info"""
        print u"""
注意 Notice：
    1. Bilibili 的番组在今天之前的两天显示的是正常的已经更新的内容，而今天之后标记的更新信息均为将要更新的内容，而不是已经更新的内容，今天则标记的是今天将要更新的内容，也可能是已经更新的，如：今天是周三，则周一、周二显示的是更新之后的内容，周四、周五、周六、周日显示的是即将更新的内容；
    2. 不显示更新信息的番剧可能是大长篇，也有可能是平台自制的节目；
    3. 今天是 {0}
        """.format(date.today().strftime('%A'))

    def cmdPrint(self, bclass):
        """Print out the Bangumi class"""
        if bclass.errorFlag:
            print (bclass.name + u' 出错啦 QAQ').encode(self.charset)
            self.errorFlag += 1
        else:
            print '--------------------------------------------------------------------------------'
            print bclass.name.encode(self.charset).center(80)
            print '--------------------------------------------------------------------------------'
            for i in range(7):
                print '===== {0} ====='.format(Tools.dow2string(i).encode(self.charset)).center(80)
                for j in bclass.bangumi[i]:
                    print j[0].encode(self.charset).rjust(38), ' -- ', j[1].encode(self.charset)

    def cmdSearch(self, bclass):
        '''Print the result to the console.'''
        keywords = []
        for keyword in self.en_keywords:
            keywords.append(keyword.decode(self.charset))
        result = bclass.search(keywords)
        if len(result) != 0:
            print '===== {0} ====='.format(bclass.name.encode(self.charset)).center(80)
            for b in result:
                print (b[1] + ' - ' + b[2] + ' - ' + Tools.dow2string(b[0])).encode(self.charset)

    def run(self):
        '''Main process'''
        # Title lol
        print u'*************************************'.encode(self.charset).center(80)
        print u'* Whoami 的中国视频网站动画番剧列表 *'.encode(self.charset).center(80)
        print u'*              命令行版             *'.encode(self.charset).center(80)
        print u'*************************************'.encode(self.charset).center(80)
        if len(self.en_keywords) == 0:
            # Print all
            self.cmdPrint(self.acfun)
            self.cmdPrint(self.bilibili)
            self.cmdPrint(self.iqiyi)
            self.cmdPrint(self.pptv)
            self.cmdPrint(self.youku)
        else:
            # Print search result
            self.cmdSearch(self.acfun)
            self.cmdSearch(self.bilibili)
            self.cmdSearch(self.iqiyi)
            self.cmdSearch(self.pptv)
            self.cmdSearch(self.youku)
        # End statistics
        print u'\n出错的网站数量：{}'.format(self.errorCount).encode(self.charset)
        self.printNotice()

if __name__ == '__main__':
    app = CLIApp(sys.argv[1:])
    app.run()
