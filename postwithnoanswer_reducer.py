#!/usr/bin/python

import sys
import csv

questionline = None
questionwithanswerline = None
oldKey = None

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    data_mapped = line

    if len(data_mapped) != 2 and len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        if not questionwithanswerline:
            print oldKey , "\t" , questionline
        oldKey = thisKey
        questionline = None
        questionwithanswerline = None

    oldKey = thisKey
    if len(data_mapped) == 2:
        questionline = data_mapped
    elif len(data_mapped) == 3:
        questionwithanswerline = data_mapped

if oldKey != None:
    if not questionwithanswerline:
        print oldKey , "\t" , questionline
