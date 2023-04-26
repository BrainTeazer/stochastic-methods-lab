#!/usr/bin/env python
# coding: utf-8

# # Brief Introduction to SciPy (part 5)
# 
# We follow the [Introduction to Scientific Python](http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf) (written by Marcel **Oliver**).
# 
# Today we discuss how to read in csv files.

from pylab import *

import csv

read = csv.reader(open('test.csv', 'r'))

data = [row for row in read]
###The line above is short for:
#data = []
#for row in read:
#    data.append(row)

print(data)

for row in data:
    print(row)

for row in data:
    if row[0] != 'Student':
        print('Student', row[0], 'achieved the grade', row[1])

