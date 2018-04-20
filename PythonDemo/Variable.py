#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100
miles = 1000.0
name = "john"

print counter
print(miles)
print name

str = 'hello world!'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "test"

# 列表
list = [ 'run-job' , 786 , 2.23 , "john" , 70.2 ]
tlist = [ 123 , "john" ]
print list
print list[0]
print list[1:3]
print list[2:]
print tlist * 2
print list + tlist

# 元组
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

# 字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

