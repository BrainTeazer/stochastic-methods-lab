import numpy as np
import timeit

# explicit loop function
def explicitLoop(C, r):
    PV = 0.0

    for i in range(len(C)):
        PV += C[i] / ( ( 1+r ) ** (i+1))

    return PV

# horner's scheme function
def horner(C, r):
    PV = 0.0
    
    for i in range(len(C) - 1, -1, -1):
        PV = (PV + C[i]) / (1.0 + r)
    
    return PV

# polyval function
def polynomial(C, r):
    C = np.insert(C, 0, 0.0)
    return np.polyval(np.flip(C),  1.0/ (1.0+r))
    
# dot product function
def dotProduct(C, r):
    i = np.arange(1, len(C) + 1)
    return np.dot(C, 1.0 / (( 1.0 + r ) ** i ))

# given values
C = 120.0 * np.arange(500,1200)
r = 0.01
evaluations = 1000

# timing each function with 1000 evaluations
t_explicit  = timeit.Timer('explicitLoop(C,r)', 'from __main__ import explicitLoop, C, r')
t_horner  = timeit.Timer('horner(C,r)', 'from __main__ import horner, C, r')
t_poly  = timeit.Timer('polynomial(C,r)', 'from __main__ import polynomial, C, r')
t_dot  = timeit.Timer('dotProduct(C,r)', 'from __main__ import dotProduct, C, r')

# printing all results 
print("Using explicit loop: ", explicitLoop(C, r), "Takes time: ", t_explicit.timeit(evaluations))
print("Using Horner's Scheme: ", horner(C,r), "Takes time: ", t_horner.timeit(evaluations))
print("Using polyval: ", polynomial(C,r), "Takes time: ", t_poly.timeit(evaluations))
print("Using vector dot product: ", dotProduct(C,r), "Takes time: ", t_dot.timeit(evaluations))

