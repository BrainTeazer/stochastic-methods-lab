import numpy as np
import matplotlib.pyplot as plt


# GBM
def S(N,T, S0, mean, std):
    dt = T/N
    
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(dt)
    dS = np.exp( (mean - (1/2) * std ** 2) * (dt) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    S = S0 * np.cumprod(dS)

    return S

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

# for varying coarsed data set
vectR = np.vectorize(r, excluded=['Si'], otypes=[float,float])

def vR(N, T, k, Si):
    return vectR(N, T, 2**np.arange(0,k+1), Si=Si)

# to vary Si
vectVR = np.vectorize(vR, otypes=[list])

def main():
    mean = 0.3
    std = 0.5
    k = 10
    samples = 1000
    N = 2 ** k
    T = 1
    S0 = 1

    Ns = (np.repeat(N+1, samples))
    intvl = 2 ** np.arange(0, k+1)
    
    Si = vS(Ns, T, S0, mean, std)
    vect = vectVR(N, T, k, Si)


    St,Mn = np.concatenate(vect, axis=1)

    Mn = Mn.reshape(-1,k+1) # getting values of Mn in array of arrays 
    St = St.reshape(-1, k+1)  # getting values of St in array of arrays 

    mnEx = np.mean(Mn, axis=0)
    mnSt = np.std(Mn, axis=0)
    stEx = np.mean(St, axis=0)
    stSt = np.std(St, axis=0)

    # actual value of Std
    actStSt = np.sqrt(stEx ** 2 / (2 * intvl)) 

    print(stSt)
    # plotting
    # starting from 2nd element to make graph more readable because stSt starts from 0
    plt.loglog(intvl[1:], stEx[1:], label='$\sigma$ mean', base=2)
    plt.loglog(intvl[1:], mnEx[1:], label='$\mu$ mean', base=2)
    plt.loglog(intvl[1:], stSt[1:], label='$\sigma$ std', base=2)
    plt.loglog(intvl[1:], mnSt[1:], label='$\mu$ std', base=2)
    plt.loglog(intvl[1:], actStSt[1:], label='exact $\sigma$ std', base=2)

    plt.legend()

    plt.show()

main()

# Yes, the statistics do reproduce the result.
# As N increases, the trend for the variance of the estimate seems very similar - but variance seems to decrease as N increases (e.g. at N = 2 ** 8 it is near 2^(-1), but for N=2 ** 15 it is near 2^(-2))

    
