import numpy as np
import matplotlib.pyplot as plt

# returns brownian paths
def brownian(N):
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(1/N)
    
    # conventionally the first value of a Brownian path is 0
    xi[0] = 0

    return np.cumsum(xi)

def main():
    # given values
    N = 600
    paths = 1000
    intvl = np.linspace(0, 1, N)
    samples = 10

    bP = [brownian(N) for path in np.arange(0, paths)]
    
    # finding mean and std
    bPMean = np.mean(bP, axis=0)
    bPStd = np.std(bP, axis=0)


    # plotting samples
    for i in np.arange(0, samples):
        plt.plot(intvl, bP[i], c='lightgreen', label='Standard Brownian Path' if i==0 else "")
    
    plt.plot(intvl, bPMean, label='Empirical Mean')
    plt.plot(intvl, bPMean + bPStd, c="blue", label='Empirical Standard Deviation')
    plt.plot(intvl, bPMean - bPStd, c="blue")

    plt.xlabel(r'Time $(t)$')
    plt.ylabel(r'Brownian Path $(W(t))$')
    plt.title(r'Standard Brownian Paths')

    plt.legend()
    plt.show()

main()
