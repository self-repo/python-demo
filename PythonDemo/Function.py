#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printInfo(name,age):
    print 'name:',name
    print 'age:',age
    return

printInfo('john',18)
printInfo(name='john',age=18)


def printABC(*value):
    for v in value:
        print 'value:',v
    return

printABC(1,2,3)


sum = lambda v1, v2: v1 + v2;
print sum(10,20)
