import numpy as np
import matplotlib.pyplot as plt

def S(N,T, S0, mean, std):
    dt = T/N
    # W(t)
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(dt)
    
    dS = np.exp( (mean - (1/2) * std *std) * (dt) + std * xi)

    # conventionally first element is S0
    dS[0] = S0

    
    exactS = S0 * np.cumprod(dS)

# -------------------------------------------------------------------------------- #

    approxS = np.zeros(len(xi))
    approxS[0] = S0 # initial value is S0

    # euler-maruyama method for len(xi) steps
    for i in np.arange(0, len(xi)-1):
        approxS[i+1] = approxS[i] + mean * approxS[i] * (dt) + std * approxS[i] * xi[i+1]


    return exactS, approxS


def monteCarlo(function, *args, samples=100):
    return np.average(
        [function(*args) for sample in np.arange(0,samples)]
    )

def strong(N, T, S0, mean, std):
    exactS, approxS = S(N, T, S0, mean, std)
    return np.absolute(exactS[-1] - approxS[-1])

def exact(N, T, S0, mean, std):
    exactS, _ = S(N, T, S0, mean, std)
    return exactS[-1]

def approx(N, T, S0, mean, std):
    _, approxS = S(N, T, S0, mean, std)
    return approxS[-1]

def main():
    mean = 1.5
    std = 0.8
    S0 = 1
    T = 1
    N = 2000
    nAvg = 15
    
    exactS, approxS = S(N, T, S0, mean, std)
    intvl = np.linspace(0, 1, N)

    allN = 2 * np.arange(1,500)
    allDt = T/allN
    
    allValExact = []
    allValApprox = []

    for oneN in allN:
        allValExact.append( 
            monteCarlo(strong, oneN, T, S0, mean, std)
        )
        
        wkE = monteCarlo(exact, oneN, T, S0, mean, std)
        wkA = monteCarlo(approx, oneN, T, S0, mean, std)
        
        allValApprox.append(np.abs(wkE - wkA))
        

    slopeE, interceptE = np.polyfit(np.log10(allDt), np.log10(allValExact), 1)
    slopeA, interceptA = np.polyfit(np.log10(allDt), np.log10(allValApprox), 1)

    print("Strong order of convergence is:", slopeE)
    print("Weak order of convergence:", slopeA)


    S(N,N/8, S0, mean, std) 
    plt.plot(intvl, exactS, label="Exact solution (GBM)", color="black")
    plt.plot(intvl, approxS, label="Approximate solution (Euler-Maruyama)", color="gray")
    
    plt.xlabel("$T$")
    plt.ylabel("$S(t)$")
    plt.legend()
    plt.show()


main()