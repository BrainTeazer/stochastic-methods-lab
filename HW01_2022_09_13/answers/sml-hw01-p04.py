from scipy import optimize
import numpy as np

def f(x, P, C, n):
    return P\
        - np.sum(C / ((1+x) ** n))

def main():
    # given values
    n = 10
    C = 120.0 * np.arange(42,52)
    P = 50000.0

    power = np.arange(1,n+1)

    # finding irr
    irr = optimize.brentq(f, 0, 1, args=(P, C, power))

    print(irr * 100, "%")

main()
