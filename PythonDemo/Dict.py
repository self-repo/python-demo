#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dict['Age']: ", dict['Age'];
print dict.get('Class-Tmp',"tmp")

print dict
del dict['Name']
print dict