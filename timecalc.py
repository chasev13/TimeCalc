#!/usr/bin/env python2.7
import sys

query = sys.argv[1].replace('') #4:03+33

time, mins = query.split('+')
mins = int(mins) # time, mins = "4:03", 30
time = map(int, time.split(':')) # time = [4,3]
time[1] = mins + time[1]
while time[1] > 59:
    time[0] += 1
    time[1] -= 60


print "{}:{}".format(time[0], time[1] if time[1] > 9 else "0" + time[1])
