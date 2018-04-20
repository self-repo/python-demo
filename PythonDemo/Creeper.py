#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def get_html(url):
    print 'get the content of the url'
    rsp = requests.get(url)
    rsp.encoding = 'utf-8'
    return rsp.text

def get_certain_joke(html):
    print 'get the joke of the html'
    soup = BeautifulSoup(html,'html')
    # print soup
    joke_content = soup.select('div.content')[0].get_text()

    print soup.select('div.content')[1].get_text()
    return joke_content

url_joke = "https://www.qiushibaike.com"
html = get_html(url_joke)
joke_content = get_certain_joke(html)
print joke_content