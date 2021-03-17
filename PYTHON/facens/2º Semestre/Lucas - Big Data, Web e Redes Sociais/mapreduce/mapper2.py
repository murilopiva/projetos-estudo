#!/usr/bin/env python

import sys

for line in sys.stdin:
    
    line = line.strip()
    words = line.split(',')
    
    print("filme id {}\t{}".format(words[1], 1))