#!/usr/bin/env python
# coding: utf-8

# # Brief Introduction to SciPy (part 4)
# 
# We follow the [Introduction to Scientific Python](http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf) (written by Marcel **Oliver**).
# 
# Today we discuss how to vectorize functions.

from pylab import *

def fct(a,b):
    if a > b:
        return 1
    else:
        return 0

A = arange(0,5)
B = [9,910,8,1,1]

#print(fct(A,B))

vec_fct = vectorize(fct)

print(vec_fct(A,B))
