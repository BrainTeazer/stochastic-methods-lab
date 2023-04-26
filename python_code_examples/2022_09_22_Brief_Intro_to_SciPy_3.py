#!/usr/bin/env python
# coding: utf-8

# # Brief Introduction to SciPy (part 3)
# 
# We follow the [Introduction to Scientific Python](http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf) (written by Marcel **Oliver**).
# 
# Today we discuss how to do nice plots. Please remember to always label your plots nicely in the homework submissions.

from pylab import *

N = 1000 # number of plot points

xmin = -2 # minimum value for x axis
xmax = 2  # maximum value for x axis

xx = linspace(xmin, xmax, N) # create the spaceing for the x axis

def f(x):
    return x**2
def g(x):
    return sin(5*x)

figure()
plot(xx,f(xx))
plot(xx,g(xx))

rc('text', usetex=True) # use TeX typesetting for all labels

figure()
plot(xx,f(xx), 'b', label="This is $x^2$") # look up more color codes in the documentation
plot(xx,g(xx), 'g', label="This is $\sin(5x)$")

xlabel("$x$")
ylabel("$f(x),g(x)$")
ylim(-1.5,3)
xlim(-2,2)
title("This is a test plot.")
legend(loc = 'upper right') # look up more options in the documentation

annotate('Parabola', xy=(1,1), xytext=(-0.5,2), size=18, arrowprops = dict(arrowstyle="->"))
axvline(-1, color='k', linestyle=':')
axhline(0, color='k')

savefig('Test_plot.pdf')

show()

