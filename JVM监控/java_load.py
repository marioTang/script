#!/usr/bin/python
import os
import re
import sys
import json
app=sys.argv[1]
option=sys.argv[2]
def jstat_gc(app,option):
    with open("/tmp/java_%s.log"%app,"r") as f:
        gc_dict = json.load(f)
        print float(gc_dict[option])
   
jstat_gc(app,option)
