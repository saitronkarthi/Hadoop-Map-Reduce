#!/usr/bin/python
#reducer.py
import sys
crimetype = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    crime,count = line.split('\t')

    if crime in crimetype:
        crimetype[crime].append(int(count))
    else:
        crimetype[crime] = []
        crimetype[crime].append(int(count))

#Reducer
for crimes in crimetype.keys():
    totalcount=sum(crimetype[crimes])
    print '%s,%s'% (crimes, totalcount)
