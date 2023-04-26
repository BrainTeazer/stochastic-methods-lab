import numpy as np
import matplotlib.pyplot as plt

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
        
    # get every 2^i-th data point
    sCoarse = Si[::int(N/k)]

    r = np.diff(np.log(sCoarse)) # log sCoarse and get pairwise difference
    var = np.var(r)
    ex = np.mean(r)


    aS = np.sqrt(var / dt) # approx Std
    aM = (ex / dt) + (aS ** 2 / 2 ) # approx Mean

    return aS, aM

# for varying coarsened data
vectR = np.vectorize(r, excluded=['Si'], otypes=[float, float])

def main():
    mean = 0.3
    std = 0.5
    k = 15
    N = 2 ** k
    T = 1
    S0 = 1
    
    # N + 1 fixes the step-sizes issue done in r that is caused when doing just N 
    Si = S(N+1, T, S0, mean, std)

    subInt = 2 ** np.arange(0, k+1, 1)

    appStd, appMean = vectR(N,T,subInt, Si=Si)
    print(appMean)

    # plotting
    plt.semilogx(subInt, appStd, base=2, label="Approximate $\sigma$")
    plt.semilogx(subInt, appMean, base=2, label="Approximate $\mu$")
    plt.axhline(std, c="gray", label="Exact $\sigma$", linestyle="dotted")
    plt.axhline(mean, c="black", label="Exact $\mu$", linestyle="dotted")


    plt.xlabel("log of number of sample points")
    plt.ylabel("$\sigma$ and $\mu$")
    plt.title("$\sigma$ and $\mu$ vs. log of number of sample points")

    plt.legend()
    plt.show()

main()
    

# Generally, std approximate value seem to converge at the exact value, but the mean approximate value does not. 
