#!/usr/bin/env python3
import re
import csv
import operator
import sys

per_users = {}
errors = {}

logfile = 'syslog.log'
f = open(logfile, 'r')

errorfile = 'error_message.csv'
userfile = 'user_statistics.csv'

for log in f:
    result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
    if result.group(2) not in errors.keys():
        errors[result.group(2)] = 0
    errors[result.group(2)] += 1
    if result.group(3) not in per_users.keys():
        per_users[result.group(3)] = {}
        per_users[result.group(3)] ["INFO"] = 0
        per_users[result.group(3)] ["ERROR"] = 0

    if result.group(1) == "INFO":
        per_users[result.group(3)] ["INFO"] += 1
    elif result.group(1) == "ERROR":
        per_users[result.group(3)] ["ERROR"] += 1

errors = sorted(errors.items(), key = operator.itemgetter(1), reverse= True)
per_users = sorted(per_users.items())

f.close()
errors.insert(0, ('Error', 'Count'))

f = open(errorfile, 'w')
for error in errors:
    a,b = error
    f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(userfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in per_users:
    a,b = stats
    f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')