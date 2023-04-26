import numpy as np
import numpy.ma as ma
from scipy.linalg import solve_banded
import timeit

def triDiagSolver(l, m, u, d):
    l = np.insert(l, 0, 0)
    u = np.insert(u, len(u), 0)

    size = len(d)
    cp = np.zeros(size-1)
    dp = np.zeros(size)
    sol = np.zeros(len(dp))
    
    cp[0] = u[0]/m[0]
    dp[0] = d[0]/m[0] 

    for i in np.arange(1,size-1):
        cp[i] = u[i]/(m[i] - cp[i-1]*l[i+1])

    for i in np.arange(1, size):
        dp[i] = (d[i] - dp[i-1] * l[i])/(m[i] - cp[i-1] * l[i])

    sol[size - 1] = dp[size-1]

    for i in np.arange(size-2, -1, -1):
        sol[i] = dp[i] - cp[i] * sol[i+1]

    return sol

def banded_f(lower,upper, banded, solv):
    return solve_banded((lower, upper), banded, solv)



evaluations = 1000
elements = 10

l = u = np.ones(elements-1) * -1
m = np.ones(elements) * 2
d = np.random.uniform(0, 1, elements)

lower = upper = 1 
    
    
banded = np.array( 
    [np.insert(u, 0, 0),
    m,
    np.insert(l, len(l), 0)]
)
    
t_tri = timeit.Timer('triDiagSolver(l,m,u,d)', 'from __main__ import triDiagSolver, l, m, u, d')
t_banded = timeit.Timer('banded_f(lower, upper, banded, d)', 'from __main__ import banded_f, lower, upper, banded, d')
   

# printing all results 
print("Using brentq: ", triDiagSolver(l, m, u, d), "Takes time: ", t_tri.timeit(evaluations))
print("Using bisection method: ", banded_f(lower, upper, banded, d), "Takes time: ", t_banded.timeit(evaluations))

