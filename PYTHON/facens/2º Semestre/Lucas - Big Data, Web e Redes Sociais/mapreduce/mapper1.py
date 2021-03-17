#!/usr/bin/env python

import sys

for line in sys.stdin:
    
    line = line.strip()
    words = line.split(',')
    
    print("nivel {}\t{}".format(words[2], 1))