#!/usr/bin/env python

import sys

def reducer():
    placeTotal = 0
    oldKey = None
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        
        thisKey, thisPlace = data
        
        if oldKey and oldKey != thisPlace:
            print "{0}\t{1}".format(oldKey, placeTotal)
            
            placeTotal = 0
            
            oldKey = placeKey
            placeTotal += "1"
            
    if oldKey != None:
        print "{0}\t{1}.format(oldKey, placeTotal)
        
  