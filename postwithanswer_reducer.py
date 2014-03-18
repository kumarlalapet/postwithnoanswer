#!/usr/bin/python

import sys
import csv

answercount = 0
oldKey = None

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    data_mapped = line

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        result = []
        result.append(oldKey)
        result.append(answercount)
        writer.writerow(result)
        #print oldKey , "\t" , answercount
        oldKey = thisKey
        answercount = 0

    oldKey = thisKey
    answercount = answercount + 1

if oldKey != None:
    result = []
    result.append(oldKey)
    result.append(answercount)
    writer.writerow(result)
    #print oldKey , "\t" , answercount
