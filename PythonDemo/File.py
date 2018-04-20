#!/usr/bin/python
# -*- coding: UTF-8 -*-

f=open('D://python/repo/PythonDemo/temp.txt','r+')

print f

print 'name:',f.name

print 'context:',f.read()

#ls = f.readlines()
#for line in ls:
#    print line
f=open('D://python/repo/PythonDemo/temp.txt','w+')
f.write("abc\n")
f.write("only-test")
f.flush()

ls = f.readlines()
for line in ls:
    print line