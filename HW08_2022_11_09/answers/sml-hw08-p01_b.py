import numpy as np
import matplotlib.pyplot as plt

def F(N,T, F0, mean, std):
    dt = T/N
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(dt)

    dS = np.exp( (mean - (1/2) * std *std) * (dt) + std * xi)

    # conventionally first element is S0
    dS[0] = F0


    S = F0 * np.cumprod(dS)

    allT = dt * np.arange(1, N+1)
    exactF = (1+allT) ** 2 * np.cos(S)

# -------------------------------------------------------------------------------- #

    approxF = np.zeros(len(xi))
    approxF[0] = 0 # initial value is S0

    # euler-maruyama method for len(xi) steps
    for i in np.arange(0, len(xi)-1):
        t = allT[i]
        
        # equation (before dt) in the pdf 
        fx = (2*approxF[i]) / (1+t) - mean * np.sqrt(np.power(1+t, 4) - approxF[i] ** 2) * np.arccos(approxF[i] / (1+t)**2)-(approxF[i] / 2) * (std * np.arccos(approxF[i] / (1 + t) **2)) ** 2

        # equation (before dW) in the pdf
        gx = std * np.arccos(approxF[i] / (1+t) ** 2) * np.sqrt(np.power(1+t,4) - approxF[i] ** 2)
        
        approxF[i+1] = approxF[i] + fx * dt - gx * xi[i+1]


    return exactF, approxF

def main():
    T = 1
    S0 = 1
    mean = 0.5
    std = 3

    N = 10000
    exactF, approxF = F(N,T,S0, mean, std)
    intvl = np.linspace(0,T,N)

    plt.plot(intvl, exactF, color="black", label="Exact value of  F")
    plt.plot(intvl, approxF, color="red", label="Approximation of F")
    plt.legend()
    plt.show()
    

main()



