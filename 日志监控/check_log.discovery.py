#!/usr/bin/python
#  -*- coding:utf-8 -*-
import json
import codecs
import sys

level = sys.argv[1]

file = open('/opt/shells/log_list')
read_f = file.readlines()

dict = {}
list = []
for line in read_f: 
    li = line.split('=')
    app_dict = {}
    if level == 'p1':
       if li[0] == 'p1':
          app_dict['{#LEVEL}'] = li[0]
          app_dict['{#COUNT}'] = int(li[1])
          app_dict['{#URL_P1}'] = li[2]
          app_dict['{#LOG_P1}'] = li[3]
          app_dict['{#DESC}'] = li[4]
          list.append(app_dict)
    elif level == 'p0':
       if li[0] == 'p0':
          app_dict['{#LEVEL}'] = li[0]
          app_dict['{#COUNT}'] = int(li[1])
          app_dict['{#URL_P0}'] = li[2]
          app_dict['{#LOG_P0}'] = li[3]
          app_dict['{#DESC}'] = li[4]
          list.append(app_dict)
    elif level == 'p2':
       if li[0] == 'p2':
          app_dict['{#LEVEL}'] = li[0]
          app_dict['{#COUNT}'] = int(li[1])
          app_dict['{#URL_P2}'] = li[2]
          app_dict['{#LOG_P2}'] = li[3]
          app_dict['{#DESC}'] = li[4]
          list.append(app_dict)
dict['data'] = list

jsonStr = json.dumps(dict,sort_keys=True,indent=4,ensure_ascii=False)
print jsonStr
