#!/usr/bin/python
# -*- coding: UTF-8 -*-

numbers = [1,2,3,4,5]
even = []
odd = []

while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print even
print odd
