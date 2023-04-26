import numpy as np
import matplotlib.pyplot as plt

def S(N, S0, mean, std):
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(1/N)

    dS = np.exp( (mean - (1/2) * std *std) * (1/N) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    return S0 * np.cumprod(dS)

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
    N1 = 500
    N2 = 600
    mean = 0.7
    std = 0.4
    S0 = 1
    T=1
    samples = 6
    intvl1 = np.linspace(0, 1, N1)
    intvl2 = np.linspace(0, 1, N2)


    # getting geometric mean
    gBP = [ S(N1, S0, mean, std) for path in np.arange(0, paths) ]

    # mean and std
    gBPMean = np.mean(gBP, axis=0)
    gBPStd = np.std(gBP, axis=0)

     # binomial tree
    bin = [ binom(N2, S0, T,mean,std) for path in np.arange(0, paths) ]

    # mean and std
    binMean = np.mean(bin, axis=0)
    binStd = np.std(bin, axis=0)

    _, ax = plt.subplots(1, 2)

    # plotting geometric brownian path
    for i in np.arange(0, samples):
        ax[0].plot(intvl1, gBP[i], c='lightgreen', label='Standard Brownian Path' if i==0 else "")

    ax[0].plot(intvl1, gBPMean, c="black", label='Empirical Mean') 
    ax[0].plot(intvl1, gBPMean+gBPStd, c="red", label='Empirical Standard Deviation') 
    ax[0].plot(intvl1, gBPMean-gBPStd,  c="red") 

    ax[0].set_title(r'Geometric Brownian Paths $S(t)$')
    ax[0].legend()

    ax[0].set_xlabel(r'Time $(t)$')
    ax[0].set_ylabel(r'Geometric Brownian Paths $S(t)$')


    # plotting binomial paths
    for i in np.arange(0, samples):
        ax[1].plot(intvl2, bin[i], c='lightblue', label='Standard Brownian Path' if i==0 else "")
    
    ax[1].plot(intvl2, binMean, c="black", label='Empirical Mean')
    ax[1].plot(intvl2, binMean+binStd, c="red", label='Empirical Standard Deviation')
    ax[1].plot(intvl2, binMean-binStd, c="red")

    ax[1].set_xlabel(r'Time $(t)$')
    ax[1].set_ylabel(r'Binomial Paths')
    ax[1].set_title(r'Binomial Tree Model (Calibrated)')

    ax[1].legend()
    plt.show()
    
main()

# The two graphs are very similar it seems that the Geometric Brownian Motion is 
# essentially the underlying model for the Binomial Tree Model for very large values of N