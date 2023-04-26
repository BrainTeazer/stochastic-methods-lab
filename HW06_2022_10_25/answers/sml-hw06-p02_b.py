import numpy as np
import matplotlib.pyplot as plt 

def binom(N, S0,T, r,std):

    # calculating u 
    u = np.exp(std * np.sqrt(T/N))
    
    d = 1/u

    # finding probability 
    p = (np.exp(r * T/N) - d) / (u-d)

    S = np.random.choice([d,u], size=N, p=[1-p, p])

    S[0]= S0

    return np.cumprod(S)

def main():
    # defining variables
    paths = 1000
    N = 600
    T = 1
    mean = 0.7
    std = 0.4
    S0 = 1
    samples = 6
    intvl = np.linspace(0, 1, N)

    # binomial tree
    bin = [ binom(N, S0, T,mean,std) for path in np.arange(0, paths) ]

    # mean and std
    binMean = np.mean(bin, axis=0)
    binStd = np.std(bin, axis=0)


    # plotting binom tree
    for i in np.arange(0, samples):
        plt.plot(intvl, bin[i], c='lightblue', label='Standard Brownian Path' if i==0 else "")

    # plotting mean and std
    plt.plot(intvl, binMean, c="black", label='Empirical Mean')
    plt.plot(intvl, binMean+binStd, c="red", label='Empirical Standard Deviation')
    plt.plot(intvl, binMean-binStd, c="red")

    plt.xlabel(r'Time $(t)$')
    plt.ylabel(r'Binomial Paths')
    plt.title(r'Binomial Tree Model (Calibrated)')

    plt.legend()

    plt.show()
    
main()