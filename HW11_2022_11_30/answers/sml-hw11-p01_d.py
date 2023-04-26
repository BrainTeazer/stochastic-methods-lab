import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

# gbm
def S(N,T, S0, mean, std):
    dt = T/N
    # W(t) 
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(dt) 

    dS = np.exp( (mean - (1/2) * std ** 2) * (dt) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    S = S0 * np.cumprod(dS)

    return S


def r(N,T, k, Si):
    dt = T / k # interval between two points

    sCoarse = Si[::int(N * dt)]

    r = np.diff(np.log(sCoarse)) # log sCoarse and get pairwise difference

    var = np.var(r)
    ex = np.mean(r)

    aS = np.sqrt(var / dt)
    aM = (ex / dt) + (aS ** 2 / 2 )

    return aS, aM

# for varying coarsened data
vectR = np.vectorize(r, excluded=['Si'])

def main():
    mean = 0.3
    std = 0.5
    k = 10
    N = 2 ** k
    T = 1
    S0 = 1
    frequency = 1.3
    
    Si = S(N, T, S0, mean, std)

    # getting gaussian and periodic noise
    gNoise = np.sqrt(1 / N) * np.random.normal(loc=0.0, scale=1.0, size=N)
    pNoise =  np.sqrt(1/N) * np.sin(2 * np.pi * frequency * np.arange(N))

    subInt = 2 ** np.arange(1, k+1)

    # approx std and mean for each GBM case
    appStd, appMean = vectR(N, T, subInt, Si=Si)
    appStdG, appMeanG = vectR(N,T, subInt, Si=Si+gNoise)
    appStdP, appMeanP = vectR(N,T, subInt, Si=Si+pNoise)

    # plotting
    _, ax = plt.subplots(1,3)

    ax[0].semilogx(subInt, appStd, base=2, label="Approximate $\sigma$")
    ax[0].semilogx(subInt, appMean, base=2, label="Approximate $\mu$")
    
    ax[1].semilogx(subInt, appStdG, base=2, label="Approximate $\sigma$")
    ax[1].semilogx(subInt, appMeanG, base=2, label="Approximate $\mu$")

    ax[2].semilogx(subInt, appStdP, base=2, label="Approximate $\sigma$")
    ax[2].semilogx(subInt, appMeanP, base=2, label="Approximate $\mu$")

    ax[0].set_xlabel("log of number of sample points")
    ax[0].set_ylabel("$\sigma$ and $\mu$")
    ax[0].set_title("No noise")
    

    ax[1].set_xlabel("log of number of sample points")
    ax[1].set_ylabel("$\sigma$ and $\mu$")
    ax[1].set_title("Gaussian noise")
  

    ax[2].set_xlabel("log of number of sample points")
    ax[2].set_ylabel("$\sigma$ and $\mu$")
    ax[2].set_title("Periodic noise")

    ax[0].legend()
    ax[1].legend()
    ax[2].legend()

    plt.show()

main()

# Mean and Standard deviation of GBM with Gaussian noise does not converge to the exact value - but for periodic noise it seems to vary greatly on the frequency. E.g. when frequency is 1 it stays quite similar to without noise. But if it is 1.3, for example, it changes much more and does not converge.
