#!/usr/bin/python
# -*- coding: UTF-8 -*-

class User:
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        User.count+=1

    def printUser(self):
        print self.name,":",self.age

    def printCount(self):
        print self.count


u1 = User('john',18)
u1.printUser()

u2 = User('cache',22)
u2.printUser()

print User.count

print '________________________________'

class Parent:
    def myMethod(self):
        print '调用父类方法'

class Child(Parent):
    def myMethod(self):
        print '调用子类方法'

c = Child()
c.myMethod()

print '________________________________'

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __cmp__(self, other):
        return self.a * self.b > other.a * other.b

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

print v1.__cmp__(v2)