#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # Brief Introduction to SciPy (part 2)
# 
# We follow the [Introduction to Scientific Python](http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf) (written by Marcel **Oliver**)

from pylab import *

### Scientific Python is optimized for vector operations! Use them whenever possible.

v = array([1,6,3,5])
print(v, v[1], 2*v, v**2, exp(v), len(v))

a = dot(v,[1,2,1,1])
b = sum(v)
print(a,b)

v2 = linspace(0,1,11)
print(v2)

# More about plotting next time, but here quickly:
x = linspace(0,2*pi,1000)
plot(x,sin(x))

v3 = arange(0,21,2)
print(v3)

v4 = arange(20)
print(v4)

v5 = r_[4:21:2]
print(v5)

v6 = c_[4:21:2]
print(v6)

print(r_[v,v**2])

# Matrices

matrix = array([[1,2],[3,4]])
print(matrix)

print(eye(7,5))
print(zeros((5,5)))
print(ones((5,5)))
print(diag(v))


#FOR loops and indexing

for i in arange(0,10):
    print(i)

for i in exp(arange(4)*3):
    print(i)


# A note on array manipulation

a = arange(20)
print(a)
print(a[3:10])
print(a[4:17:2])
print(a[17:4:-1])
print(a[::-1])



### Formatting output

print("{0:10.5f}".format(4363.85738282))
print("|{some_number:10.5f}|".format(some_number = 4363.85738282))
print("|{0:10.2f}|{1:10.2f}|{2:10.2f}|".format(4363.85738282, 47728.9482727, 8989.29292929))
print("|{0:10d}|".format(423))
print("{0:e}".format(29**8))

# => numerous possibilities for formatting, just look up what you need

# a simple table:
b = linspace(0,1,13)
for i in arange(0,13):
    print("|{0:<10d}|{1:10.3f}|{2:10.2f}|".format(i,b[i],b[i]**2))


### A note of caution: variable assignment in python is by reference!

a = array([1,1,1])
print(a)
b = a
#b = a.copy() # if you want to force a copy
a[0] = 42
print(a)
print(b)
# arrays are mutable objects: they are just references to some memory region
# (this makes sense if you are dealing with large data sets)

a = pi
b = a
a = 42
print(a)
print(b)
# some constants and numbers and strings are immutable
