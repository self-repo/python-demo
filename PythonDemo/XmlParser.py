#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "movie":
            print "***movie***"
            title = attributes["title"]
            print 'title:',title

    def endElement(self, tag):
        print 'enter end element.',self,tag
        if self.currentData == "type":
            print 'type:',self.type
        elif self.currentData == "format":
            print 'format:',self.format
        elif self.currentData == "year":
            print 'year:',self.year
        elif self.currentData == "rating":
            print 'rating:',self.rating
        elif self.currentData == "stars":
            print 'stars:',self.stars
        elif self.currentData == "description":
            print 'description:',self.description
        self.currentData = ""

    def characters(self, content):
        print 'enter characters.',self,content
        if self.currentData == "type":
            self.type = content
        elif self.currentData == "format":
            self.format = content
        elif self.currentData == "year":
            self.year = content
        elif self.currentData == "rating":
            self.rating = content
        elif self.currentData == "stars":
            self.stars = content
        elif self.currentData == "description":
            self.description = content

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = MovieHandler()
parser.setContentHandler(handler)

parser.parse("D://python/repo/PythonDemo/movies.xml")



















