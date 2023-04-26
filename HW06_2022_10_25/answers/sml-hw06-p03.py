from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt 

# payoff function
def payoff(S, K, opt='C'):
    if opt.upper() == 'C':
        return np.maximum(S-K, 0)
    elif opt.upper() == 'P':
        return np.maximum(K-S, 0)

# blackScholes
def blackScholes(S, K, T, r, sigma):
    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))

    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))

# sample geomtric Brownian Motion
def S(N, S0,T,K, mean, std):
    # final path
    S = S0 * np.exp((mean - (1/2)*(std**2))*T + std*np.sqrt(T)*np.random.normal(loc=0.0, scale=1.0))
    return np.max(S-K, 0)

# get the average (expected) value of N samples
def monteExpected(N, S0, T, K, mean, std):
    return np.sum([S(no,S0,T,K, mean, std) for no in np.arange(0,N)])/N

def main():
    mean = 0.3
    std = 0.7
    K = 0.8
    T = 1
    S0 = 1
    N = 1000

    bSPrice = blackScholes(S0, K, T, mean, std)
    mCPrice = [monteExpected(i, S0, T, K, mean, std) for i in np.arange(1,N+1)]

    allBSPrice = np.ones(N) * bSPrice

    diff = np.abs(mCPrice - allBSPrice)

    vals = np.arange(1, N+1)
    loggedDiff = np.log10(diff)
    loggedVal = np.log10(vals)

    slope, intercept = np.polyfit(loggedVal, loggedDiff, 1)
    print("The rate of convergence is: ", slope)

    plt.plot(np.log10(vals), np.log10(diff), label="Single log plot")
    plt.plot(np.log10(vals), slope * np.log10(vals) + intercept, label="Doubly log plot")

    plt.title("Doubly logged plot vs singly logged plot")

    plt.legend() 
    plt.show()

main()

