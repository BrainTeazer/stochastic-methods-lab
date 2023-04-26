from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def binomial_tree(payoff, n, rp, sigma, S, K, T):
    tt = T/n
    u = np.exp(sigma * np.sqrt(tt))
    d = 1 / u

    q = (np.exp(rp * tt) - d) / (u-d)

    S1 = S * d ** (np.arange(n, -1, -1)) * u ** (np.arange(0, n+1, 1))
    poff = payoff(S1, K)

    for i in np.arange(n, 0, -1):
        poff = np.exp(-rp * tt) * (q * poff[1:i+1] + (1-q) * poff[0:i])

    return poff[0]

# payoff function
def payoff(S, K, opt='C'):
    if opt.upper() == 'C':
        return np.maximum(S-K, 0)
    elif opt.upper() == 'P':
        return np.maximum(K-S, 0)

def blackScholes(S, K, T, r, sigma):
    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))

    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))

def main():
    S = 1
    K = 1.2
    sigma = 0.5
    T = 1
    rp = 0.03
    n = np.arange(1, 101)

    binomTree = [binomial_tree(payoff, itr, rp, sigma, S, K, T) for itr in n]
    blackSchole = blackScholes(S, K, T, rp, sigma)
    allBlackSchole = np.empty(n.size)
    allBlackSchole.fill(blackSchole)

    relError = np.absolute(allBlackSchole - binomTree)

    slope, intercept = np.polyfit(np.log10(n), np.log10(relError), 1)
    refLine = lambda x: np.power(10, slope * x + intercept)

    plt.loglog(n, relError)
    plt.loglog(n, refLine(np.log10(n)) )
    plt.xlabel(r'$n$ in $log$ scale')
    plt.ylabel(r'rel. error in $log$ scale')

    plt.title(r"LogLog plot of rel. error vs $n$")

    print("The error scales with approximately n to the power of {} or approximately 1/n".format( slope))

    plt.show()

main()


"""

The graph obtained is downward trending, which is similar to a straight line - though it is not a straight line. 
However, in the beginning it is approximately a straight line in the beginning.

"""
