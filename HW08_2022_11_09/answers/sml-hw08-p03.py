import numpy as np
import matplotlib.pyplot as plt

def brownian(N,T):
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(T/N)

    # conventionally the first element is 0
    xi[0] = 0

    return np.cumsum(xi)

def crossValue(N, T):
    brown = brownian(N,T)
    try:
        # get first index where condition is met and find the corresponding time
        return np.where(np.logical_or(brown>1, brown < -1))[0][0] * T/N 
    except:
        # if none meet the condition return 0
        return T

def monteCarlo(function, *args, samples=100):
    return [function(*args) for sample in np.arange(0,samples)]

def main():
    T = 5
    N = 800

    monte_carlo = monteCarlo(crossValue, N, T, samples=1000)
    E_hitting_time = np.average(monte_carlo)
    V_hitting_time = np.var(monte_carlo)

    print("Expectation: ", E_hitting_time)
    print("Variance: ", V_hitting_time)


main()
