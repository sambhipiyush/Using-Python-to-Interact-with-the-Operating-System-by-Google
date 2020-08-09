#!/usr/bin/env python3

import re
import operator
import os
import csv

error_msg = {}
user_stat = {}

error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
info_pattern = r'ticky: INFO.* \((.+)\)'

with open('syslog.log','r') as logs:
  for line in logs.readlines():
    if re.search(error_pattern,line):
      extracts = re.search(error_pattern, line)
      error_msg.setdefault(extracts.group(1),0)
      error_msg[extracts.group(1)]+=1
      user_stat.setdefault(extracts.group(2),[0,0])[1]+=1
    if re.search(info_pattern,line):
      extracts = re.search(info_pattern, line)
      user_stat.setdefault(extracts.group(1),[0,0])[0]+=1

error_sorted = sorted(error_msg.items(), key = operator.itemgetter(1), reverse = True)
user_sorted = sorted(user_stat.items())
print(error_sorted)
print(user_sorted)

with open('error_message.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Error','Count'])
  writer.writerows(error_sorted)

with open('user_statistics.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Username','INFO','ERROR'])
  for item in user_sorted:
      onerow = [item[0],item[1][0],item[1][1]]
      writer.writerow(onerow)
