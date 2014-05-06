#! /usr/bin/env python

import glob
import re

files = {}
for fpath in glob.glob("*.txt"):
    with open(fpath) as f:
         fixed_text = re.sub("[^a-zA-Z'-]"," ",f.read())
    files[fpath] = (len(fixed_text.split()),len(set(fixed_text.split())))
    print "Total Words:" , len(fixed_text.split())
    print "Total Unique:",len(set(fixed_text.split()))

with open("wordstats.csv", "w") as f:
    for fname in files:
        print >> f , "%s,%s,%s"%(fname,files[fname][0],files[fname][1])