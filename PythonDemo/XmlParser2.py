#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("D://python/repo/PythonDemo/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element : %s" % collection.getAttribute("shelf")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")

    type = movie.getElementsByTagName('type')[0]
    print "Type: %s" % type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print "Format: %s" % format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print "Description: %s" % description.childNodes[0].data


class Movie():
    def __init__(self, title, type, format, rating, description):
        self.title = title
        self.type = type
        self.format = format
        self.rating = rating
        self.description = description

    def printMovie(self):
        print self.title+","+self.type+","+self.format+","+self.rating+","+self.description

print '________________________________________________'

list = []

for movie in movies:
    _title = ""
    if movie.hasAttribute("title"):
        _title = movie.getAttribute("title")

    type = movie.getElementsByTagName('type')[0]
    _type = type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    _format = format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    _rating = rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    _description = description.childNodes[0].data
    t = Movie(_title,_type,_format,_rating,_description)
    t.printMovie()
    list.append(t)

print '________________________________________________'
for tmp in list:
    tmp.printMovie()















