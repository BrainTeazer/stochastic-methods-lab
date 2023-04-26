import numpy as np
import matplotlib.pyplot as plt 

# brownian paths
def brownian(N,T):
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(T/N)
    xi[0] = 0
    return np.cumsum(xi)


# ito integral
def itoInt(brownian, N):
    w = brownian
    iInt = [w[i] * (w[i+2] - w[i]) for i in np.arange(0, 2*N,2)]
    return np.cumsum(iInt)

# strat integral
def stratInt(brownian, N):
    w = brownian
    sInt= [w[i+1] * (w[i+2] - w[i]) for i in np.arange(0, 2*N,2)]

    return np.cumsum( sInt )


def main():
    # setting variables
    N = 30000
    T = 1 
    
    b = brownian(2*N + 2,T)
    i = itoInt(b, N)
    s = stratInt(b, N)
    
    plt.plot(np.linspace(0,T,N), b[0:2*N:2], label="brownian")
    plt.plot(np.linspace(0,T,N), i, label="ito", c="red")
    plt.plot(np.linspace(0,T,N), s, label="strat", c="yellow")

    plt.legend()
    plt.show()

main()

# for large N's, the stratonovich integral is clearly greater than the ito integral