#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import urllib2
import sys

uri = sys.argv[1]
data = sys.argv[2]
host = '127.0.0.1'
#Url = 'http://%s:8080/channeladaptation/XmInterf' % (host,)
Url = 'http://%s:%s' % (host,uri)
update = "on"
#update = "off"

def check(Url):
    try: 
        headers = { "User-Agent":"check_url script" }
        if data == "GET":
            url = urllib2.Request(Url)
            response = urllib2.urlopen(url)  
        else:
            url = urllib2.Request(Url,data,headers)
            response = urllib2.urlopen(url)  
        http_code = response.getcode()
        print http_code
    except urllib2.HTTPError, e:
        print e.code
    except :
        print int('1234')

if update == "on":
   check(Url)
else:
   print int(666)