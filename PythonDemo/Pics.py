#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import re
import os

weburl = "http://36kr.com/" #爬取网页
tardir = "D:\\python\\pics"     #保存路径


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def destDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    p = path.split('\\')[-1]
    if not (p == ''):
        path = path + '\\'
    return path


def getSuffix(fileurl):
    return fileurl.split('.')[-1]


def getImg(html):
    reg = r'(http.:[\S]*?.(jpg|jpeg|png|gif|bmp|JPG|JPEG|PNG|GIF|BMP))'
    imgall = re.findall(reg, html)
    destPath = destDir(tardir)
    x = 1
    for imgurl, i in imgall:
        urllib.urlretrieve(imgurl, destPath + '%s.' % x + getSuffix(imgurl))
        print "完成 ".decode('UTF-8').encode('GBK') + imgurl
        x += 1


html = getHtml(weburl)
print getImg(html)
os.system("pause")