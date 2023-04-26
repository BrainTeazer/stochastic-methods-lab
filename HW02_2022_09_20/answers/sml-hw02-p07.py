import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

def horizon(r,F,c, h, n, m):
    C = F * c / m
    i = np.arange(1, n*m + 1)
    y = r/m 

    return np.sum(C / (1+y) ** (i - h)) + F/(1+y) ** (n*m - h)

def main():
    n = 30
    c = 0.1
    m = 1
    h = 10
    F = 1

    yields = np.linspace(0.0, 0.3, 100)
    futVals = []

    for yield_ in yields:
        futVals.append(horizon(yield_, F, c, h, n, m))
    

    plt.plot(yields, futVals)
    plt.show()


    minimum = optimize.brent(horizon, (F,c,h,n,m)) 
    horizonMinimum = horizon(minimum, F, c, h, n, m)
    print("The minimum is at yield={}. The value is {}.".format(minimum, horizonMinimum))

main()
