#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

if os._exists('abc.txt'):
    os.rename('abc.txt', 'abc2.txt')