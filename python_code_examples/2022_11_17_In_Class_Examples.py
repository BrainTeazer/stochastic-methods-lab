#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Color plotting of arrays and masks
"""
from pylab import *

# General stuff

S = arange(0,13)

print(ones_like(S))
print(ones(len(S)))

print(arange(6)[:,newaxis])
print(arange(6)[newaxis,:])
A = arange(6)[:,newaxis]>arange(6)[newaxis,:]

print(A)

B = arange(1,9)
print(B,roll(B,2))


# Color plots of arrays

n = 10

x = arange(0,n+1)
y = arange(0,n+1)

C = x[newaxis,:]**2 + 4*y[:,newaxis]

print(C)

figure()

imshow(C,cmap=cm.gnuplot,aspect='1',extent=(0,10,20,30),interpolation='gaussian')    

colorbar()

show()

imshow(C,norm=matplotlib.colors.LogNorm())
colorbar()
show()




# Masked arrays

D = array([[1,2],[3,4]])

print(D)

E = ma.masked_array(D,mask=[[1,0],[0,1]])

print(E)

imshow(D)
show()
imshow(E)
show()

C_mask = ma.masked_array(C,mask=ones((n+1,n+1))-eye(n+1))

imshow(C_mask)
show()