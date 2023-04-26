import numpy as np
from scipy import optimize
import timeit

CONST_ERROR = 0.000001

#function
def f(x, C, N, P):
    return P\
            - np.sum(C / ((1.0+x) ** N))

#derivative of function
def df(x, C, N, P):
    return - np.sum(C * (-N * (1+x) ** (-N - 1)))

#check if bisection interval is valid
def valInterval_b(f,  start, end, args=()):
    return f(start, *args) * f(end, *args) < 0

def bisectionMethod(f, start, end, args=(), error = CONST_ERROR):
    if not valInterval_b(f, start, end, args):
        print(" f({}) * f({}) not negative ").format(start, end)

    while abs(end - start) > error:
        mid = (start + end) / 2.0

        if  f(mid, *args) == 0:
            return mid

        if valInterval_b(f, start, mid, args):
            end = mid
        else:
            start = mid

    return mid

def newtonMethod(f, x0, fprime, args=(), error = CONST_ERROR):
    xn = x0 - f(x0, *args)/fprime(x0, *args)

    while abs(xn - x0) > error:
        x0 = xn
        xn = x0 - f(x0, *args)/fprime(x0, *args)

    return xn
    
def secantMethod(f, x0, x1, args=(), error = CONST_ERROR):
    xn = x1 - f(x1, *args) * (x1 - x0) / float (f(x1, *args) - f(x0, *args))

    while abs(x0 - x1) > error:
         
        x0 = x1
        x1 = xn

        if float(f(x1, *args) - f(x0, *args)) == 0:
            return x1

        xn = x1 - f(x1, *args) * (x1 - x0) / float (f(x1, *args) - f(x0, *args))

    return xn

def brentq_(f, a, b, args=()):
    return optimize.brentq(f, a, b, args)


# ans: 13.797958971132706%
N = 300.0
C = 120.0 * np.arange(10, N+10)
P = 15000.0
evaluations = 1000
power = np.arange(1, N+1)


t_brentq = timeit.Timer('brentq_(f,0.0,1.0,args=(C,power,P))', 'from __main__ import brentq_, f, C, power, P')
t_bisection = timeit.Timer('bisectionMethod(f, 0.0, 1.0, (C, power, P))', 'from __main__ import bisectionMethod, f, C, power, P')
t_newton = timeit.Timer('newtonMethod(f, 0.2, df, (C,power, P))', 'from __main__ import newtonMethod, f, df, C, power, P')
t_secant = timeit.Timer('secantMethod(f,0.1, 0.2, (C, power, P))', 'from __main__ import secantMethod, f, C, power, P')

# printing all results 
print("Using brentq: ", optimize.brentq(f, 0.0, 1.0, (C,power,P)) * 100, "Takes time: ", t_brentq.timeit(evaluations))
print("Using bisection method: ", bisectionMethod(f, 0.0, 1.0, (C, power, P)) * 100, "Takes time: ", t_bisection.timeit(evaluations))
print("Using newton method: ", newtonMethod(f, 0.0, df, (C,power,P)) * 100, "Takes time: ", t_newton.timeit(evaluations))
print("Using secant method: ", secantMethod(f, 0.1, 0.2, (C, power, P)) * 100, "Takes time: ", t_secant.timeit(evaluations))
