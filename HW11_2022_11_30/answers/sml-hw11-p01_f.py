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
    pNoise = np.sqrt(1/N) * np.sin(2 * np.pi * frequency * np.arange(N))

    # log return of GBM cases
    gNLogRet = np.diff(np.log(Si + gNoise))
    pNLogRet = np.diff(np.log(Si + pNoise))
    regLogRet = np.diff(np.log(Si))

    # plotting
    _, ax = plt.subplots(1,3)
    ax[0].acorr(regLogRet, maxlags=30)
    ax[1].acorr(gNLogRet, maxlags=30)
    ax[2].acorr(pNLogRet, maxlags=30)

    ax[0].set_title("ACF - No noise")
    ax[1].set_title("ACF - Gaussian noise")
    ax[2].set_title("ACF - Periodic noise")

    plt.show()




main()


#It seems that for GBM - there is little to no autocorrelation
#But, with Gaussian Noise - there seems to be auto-correlation on the point where the x coordinate is 1 (from hovering over graph)
#With periodic noise - there is autocorrelation which seems to be periodic/repeat
