#!/usr/bin/python
import os
import sys
import re
import json
import codecs
import commands

dicts = {}
lists = []
status, output = commands.getstatusoutput("ps aux |grep java|grep -v grep |grep java|awk '{print $2}'")

for j in output.split('\n'):
    pid=j
    gc = os.popen('/app/java/jdk1.8.0_141/bin/jstat -gc %s' % pid)
    gc_srt = gc.read()
    threads = os.popen('grep Threads /proc/%s/status' % pid.strip())
    threads_srt = threads.read().strip().split(':\t')
    statm = os.popen('cat /proc/%s/statm' % pid.strip())
    statm_srt = statm.read().strip().split(' ')
    statm_dict = dict(enumerate(statm_srt))
    list = re.sub(r'\s+', ' ', gc_srt).strip().split(' ')
    gc_dict = {}
    v = len(list) / 2
    for i in range(len(list) / 2):
        gc_dict[list[i]] = list[v]
        v += 1
    gc_dict[threads_srt[0]] = threads_srt[1]
    gc_dict = dict(gc_dict, **statm_dict)
    with open("/tmp/java_%s.log" % pid, "w") as f:
        json.dump(gc_dict, f)

    app_dict = {}
    app_dict['{#JAVA_PID}'] = j
    lists.append(app_dict)
dicts['data'] = lists
jsonStr = json.dumps(dicts, sort_keys=True, indent=4, ensure_ascii=False)
print (jsonStr)

