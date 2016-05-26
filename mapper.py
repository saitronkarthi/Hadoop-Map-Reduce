#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line)>0:
        print '%s\t%s' % (line[4], 1)
