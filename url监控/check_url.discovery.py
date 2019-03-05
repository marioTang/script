#!/usr/bin/python
#  -*- coding:utf-8 -*-
import json
import codecs
import sys

level = sys.argv[1]

file = open('/opt/shells/uri_list')
read_f = file.readlines()

dict = {}
list = []
for line in read_f: 
    li = line.split(' ')
    app_dict = {}
    if level == 'p1':
       if li[0] == 'p1':
          app_dict['{#URL_P1}'] = li[1]
          app_dict['{#METH_P1}'] = li[2]
          app_dict['{#DESC}'] = li[3]
          app_dict['{#LEVEL}'] = li[0]
          list.append(app_dict)

    elif level == 'p3':
       if li[0] == 'p3':
          app_dict['{#URL_P3}'] = li[1]
          app_dict['{#METH_P3}'] = li[2]
          app_dict['{#DESC}'] = li[3]
          app_dict['{#LEVEL}'] = li[0]
          list.append(app_dict)
dict['data'] = list

jsonStr = json.dumps(dict,sort_keys=True,indent=4,ensure_ascii=False)
print jsonStr
