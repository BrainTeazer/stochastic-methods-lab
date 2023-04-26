import numpy as np
import matplotlib.pyplot as plt

# a)
def GBM(N, T, S0, mean, std):
    dt = T / N

    xi = np.random.normal(loc=0, scale=1, size=N) * np.sqrt(dt)

    dS = np.zeros(N)
    dS[0] = S0 # initial value is S0

    # euler-maruyama method for len(xi) steps
    for index, val in enumerate(dS[:-1]):
        dS[index+1] = dS[index] + mean * dS[index] * (dt) + std * dS[index] * xi[index+1]

    return dS

def X(N, T, X0, mean, std, c):
    dt = T/N

    xi = np.random.normal(loc=0, scale=1, size=N) * np.sqrt(T/N)
    # dW
    dX = np.zeros(N)
    dX[0] = X0 # initial value is X0

    # euler-maruyama method for N-1 steps
    for index, val in enumerate(dX[:-1]):
        fx = mean * (1 - c*np.log(val)) * val
        gx = std * val

        dX[index+1] = val + fx * dt + gx * xi[index+1]

    return dX

def getSamples(function, *args, samples=10):
    return [X(*args) for sample in np.arange(samples)]

def main():
    # values 
    N = 1000
    T = 1
    cs = [0.01, 0.50, 0.99] 
    intvl = np.linspace(0, T, N)
    X0 = 1
    mean = 3
    std = 0.2


    _, ax = plt.subplots(1, len(cs))

    for id, c in enumerate(cs):
        # get gbm
        gbm = GBM(N, T, X0, mean, std)

        # get 10 samples for each value of c
        Xts = getSamples(X, N, T, X0, mean, std, c)

        # get mean and standard deviation of the samples
        mX = np.mean(Xts, axis=0)
        sX = np.std(Xts, axis=0)

        # plot the samples
        for i, Xt in enumerate(Xts):
            ax[id].plot(intvl, Xt, c="gold", label=f"Samples with c={c}" if i==0 else "")

        # plot mean, std, and legend
        ax[id].plot(intvl, mX, label="Empirical Mean")
        ax[id].plot(intvl, mX - sX, c="blue", label="Standard Deviation")
        ax[id].plot(intvl, mX + sX, c="blue")
        ax[id].plot(intvl, gbm, c="black", label="GBM")
        ax[id].legend()

    
    print("As c approaches 0 - the value gets closer to GBM (as the formula becomes that of the GBM). As c approaches 1 - the value get more different compared to GBM")

    plt.show()


main()
    
