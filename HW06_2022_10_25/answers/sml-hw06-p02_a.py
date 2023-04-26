import numpy as np
import matplotlib.pyplot as plt

def S(N, S0, mean, std):
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(1/N)

    dS = np.exp( (mean - (1/2) * std *std) * (1/N) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    return S0 * np.cumprod(dS)

def main():
    # defining variables
    paths = 1000
    N = 500
    mean = 0.7
    std = 0.4
    S0 = 1
    samples = 6
    intvl = np.linspace(0, 1, N)


    # getting geometric mean
    gBP = [ S(N, S0, mean, std) for path in np.arange(0, paths) ]

    # mean and std
    gBPMean = np.mean(gBP, axis=0)
    gBPStd = np.std(gBP, axis=0)

    # plot paths
    for i in np.arange(0, samples):
        plt.plot(intvl, gBP[i], c='lightgreen', label='Standard Brownian Path' if i==0 else "")

    # plot mean and std
    plt.plot(intvl, gBPMean, label='Empirical Mean')
    plt.plot(intvl, gBPMean+gBPStd, c="blue", label='Empirical Standard Deviation')
    plt.plot(intvl, gBPMean-gBPStd, c="blue")

    plt.xlabel(r'Time $(t)$')
    plt.ylabel(r'Geometric Brownian Paths $(S(t))$')
    plt.title(r'Standard Geometric Brownian Paths')

    plt.legend()

    plt.show()
    
main()