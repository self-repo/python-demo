#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

print time.time()
print time.localtime()
print time.localtime(time.time())

print time.asctime(time.localtime(time.time()))

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

print '-------------------------------------'

import calendar

cal = calendar.month(2018, 4)
print "以下输出2018年4月份的日历:"
print cal;


import datetime

print datetime.datetime.now()