import numpy as np 
from scipy import optimize


def P(r, F, c, d, n, m):
    C = F * c / m
    i = np.arange(1, m*n+1)

    return np.sum(C / (1 + r/m)**i)\
        + F / (1 + r/m)**(n*m)\
        - d*F

def main():
    m = 2
    n = 10
    F = 1.0 #value of F does not change the result substantially
    c = 0.10
    percOfPar = 0.75

    ytm = optimize.brentq(P, 0.0, 1.0, args=(F, c, percOfPar, n, m))
    print("Yield to maturity is {}%".format(ytm * 100))


main()
