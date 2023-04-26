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

# from assignment 5
def X(J):
    return (J - np.mean(J))/np.std(J)

def main():
    mean = 0.3
    std = 0.5
    k = 10
    N = 2 ** k
    T = 1
    S0 = 1
    frequency = 1.3
    
    Si = S(N, T, S0, mean, std)

    # get gNoise and pNoise
    gNoise = np.sqrt(1 / N) * np.random.normal(loc=0.0, scale=1.0, size=N)
    pNoise = np.sqrt(1/N) * np.sin(2 * np.pi * frequency * np.arange(N))
    
    # log return of each case of GBM
    gNLogRet = np.diff(np.log(Si + gNoise))
    pNLogRet = np.diff(np.log(Si + pNoise))
    regLogRet = np.diff(np.log(Si))


    normDLogRet = np.random.normal(loc=0.0, scale=1.0, size=N-1)

    normDist = np.sort(X(normDLogRet)) #normal dist
    gN = np.sort(X(gNLogRet)) # gbm with gaussian noise
    pN = np.sort(X(pNLogRet)) # gbm with perioidic noise
    reg = np.sort(X(regLogRet)) # gbm with no noise

    # plotting
    plt.plot(normDist, normDist)
    plt.scatter(normDist, gN, s=3, label='gaussian noise')
    plt.scatter(normDist, pN, s=3, label='periodic noise')
    plt.scatter(normDist, reg, s=3, label='no noise')

    plt.legend()

    plt.show()


main()

# Gaussian noise seems to very minorly, if at all, change the distribution.
# Periodic noise seems to more clearly change the distribution.
# Without any noise, the GBM stays approximately on the normal distribution line
