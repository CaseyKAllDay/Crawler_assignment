#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        acro, name, place = data
        print "{0}\t{1}".format(name, place)
        
