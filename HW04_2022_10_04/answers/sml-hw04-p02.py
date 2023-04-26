import numpy as np

# binomial tree european
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


def main():
    S = 1
    K = 0.7
    rp = 0.02
    T = 1
    n = 1000
    sigma = 0.5
    print(binomial_tree(payoff, n, rp, sigma, S, K, T))

main()
