#!/usr/bin/env python3

import sys
import subprocess

f = open(sys.argv[1], "r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
f.close()
