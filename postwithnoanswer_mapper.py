#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:

    if len(line) > 2:    
        idfield,title,tag,authid,body,nodetype,pid,apid,addedat,score,sstr,leid,labid,laat,arid,extra,exrid,excnt,mkd = line
    
        if idfield == "id":
            continue

        if nodetype == "question":
            result = []
            result.append(idfield)
            result.append("question")
            writer.writerow(result)

    elif len(line) == 2:
        idfield,noofanswers = line
        result = []
        result.append(idfield)
        result.append("question")
        result.append(noofanswers)
        writer.writerow(result)
