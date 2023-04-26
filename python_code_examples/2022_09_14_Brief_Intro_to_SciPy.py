#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # Brief Introduction to SciPy
# 
# We follow the [Introduction to Scientific Python](http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf) (written by Marcel **Oliver**)


print("Hello World.", 5, "is a number.")

print("This is a very long line")

#Print("Hello?")

######

#Import most necessary packages for Scientific Computing
from pylab import *

print(3*7, 2**5, cos(2*pi), exp(3), pi, exp(1))

print(2<4, 3==4)

print(2/3)

def some_fct(x):
    return x**2
    #notice the indent

print(some_fct(5))

######

# Timing

def f(x):
    return cos(x)

# best, runs function in a controlled environment
y = 5
import timeit
t = timeit.Timer('f(y)', 'from __main__ import f,y')
print("100000 evaluation take", t.timeit(number=100000), "s")

# alternative (simple time stamp)
import time
t = time.time()
f(190328340184533)
print("Evaluation takes", time.time()-t, "s")