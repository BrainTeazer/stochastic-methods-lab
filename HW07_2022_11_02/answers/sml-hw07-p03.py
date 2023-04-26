import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# payoff function
def payoff(S, K, opt='C'):
    if opt.upper() == 'C':
        return np.maximum(S-K, 0)
    elif opt.upper() == 'P':
        return np.maximum(K-S, 0)

# black Scholes
def blackScholes(S, K, T, r, sigma):
    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))

    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))

def main():
    T = 1
    S = 1
    K = 1.2
    N = 1000
    r = 0.03
    sigma = 0.5
    
    maxVar = 1

    varX = np.linspace(maxVar/N, maxVar, N-1)

    bSStock = blackScholes(varX, K, T, r, sigma)
    bSInterest = blackScholes(S, K, T, varX, sigma)
    bSVol = blackScholes(S, K, T, r, varX)

    _, ax = plt.subplots(1, 3)

    # plotting call price against stock price
    ax[0].plot(varX, bSStock, color="green", label="Black Scholes varied stock price $S$")
    ax[0].set_title(r'Call Price ($) against Stock Price')
    ax[0].set_xlabel(r'Stock Price ($)')
    ax[0].set_ylabel(r'Call Price ($)')
    ax[0].legend()

    # plotting call price against interest rate
    ax[1].plot(varX, bSInterest, color="red", label="Black Scholes varied interest rate $r$")
    ax[1].set_title(r'Call Price ($) against Interest Rate')
    ax[1].set_xlabel(r'Interest Rate')
    ax[1].set_ylabel(r'Call Price ($)')
    ax[1].legend()

    # plotting call price against volatility
    ax[2].plot(varX, bSVol, color="orange",label="Black Scholes varied volatility $\sigma$")
    ax[2].set_title(r'Call Price ($) against Volatility')
    ax[2].set_xlabel(r'Volatility ($\sigma$)')
    ax[2].set_ylabel(r'Call Price ($)')
    ax[2].legend()

    plt.show()


main()
