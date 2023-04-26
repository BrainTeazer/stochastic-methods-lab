import numpy as np
import matplotlib.pyplot as plt


def S(N,T, S0, mean, std):
    dt = T/N
    
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(dt)
    dS = np.exp( (mean - (1/2) * std ** 2) * (dt) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    S = S0 * np.cumprod(dS)

    return S

# vectorsing gbm to get multiple paths
vS = np.vectorize(S, otypes=[list])


def r(N,T, k, Si):
    dt = T / k # interval between two points
    sCoarse = Si[::int(N * dt)]

    r = np.diff(np.log(sCoarse)) # log sCoarse and get pairwise difference
    var = np.var(r)
    ex = np.mean(r)

    aS = np.sqrt(var / dt)
    aM = (ex / dt) + (aS ** 2 / 2 )

    return aS, aM

# vectorizing r 
trueVectR = np.vectorize(r)

def main():
    mean, std = 0.3, 0.5
    k = 10
    N = 2 ** k
    T = S0 = 1
    samples = 1000
    bins = 126
    
    Si = S(N, T, S0, mean, std)

    appStd, appMean = r(N,T, k, Si=Si)

    Ns = (np.repeat(N, samples))

    allSi = vS(N=Ns, T=T, S0=S0, mean=appMean, std=appStd)
    St, Mn = trueVectR(N, T, k, allSi)

    # plotting
    _, ax = plt.subplots(1, 2)

    ax[0].hist(St, bins)
    ax[0].axvline(std, c='black', linestyle='dashed', label='actual value' )
    ax[0].axvline(np.mean(St) + np.std(St), c='gold', linestyle='dashed', label='standard deviation value')
    ax[0].axvline(np.mean(St) - np.std(St), c='gold', linestyle='dashed')
    ax[0].set_xlabel('$\sigma$')
    ax[0].legend()
    ax[0].set_title("Histogram of $\sigma$")
    
    ax[1].hist(Mn, bins)
    ax[1].axvline(mean, c='black', linestyle='dashed', label='actual value')
    ax[1].axvline(np.mean(Mn) + np.std(Mn), c='gold', linestyle='dashed', label='standard deviation value')
    ax[1].axvline(np.mean(Mn) - np.std(Mn), c='gold', linestyle='dashed')
    ax[1].set_xlabel('$\mu$')
    ax[1].legend()
    ax[1].set_title("Histogram of $\mu$")

    plt.show()

main()

