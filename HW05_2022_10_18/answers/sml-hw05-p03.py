from scipy import special
import numpy as np
import matplotlib.pyplot as plt

# binomial distribution
def binomDist(j, n, p):
    return special.binom(n,j) * p ** j * (1-p)**(n-j)

# gaussian distribution
def guassian(x):
    return (1 / ( np.sqrt(2*np.pi) )) * np.exp(-x**2/2)

# calculate x_j
def xj(j, n, p):
    return (j -  n*p)/np.sqrt(n*p*(1-p))

# calculate y_j
def yj(j, n, p):
    return np.sqrt(n * p * (1-p)) * binomDist(j,n,p)


def main():
    n1 = 10
    n2 = 100
    p1 = 0.2
    p2 = 0.5

    j1 = np.arange(0, n1+1)
    j2 = np.arange(0, n2+1)

    
    x_n1_p1 = xj(j1, n1, p1) # x: n=10 p=0.2
    x_n1_p2 = xj(j1, n1, p2) # x: n=10 p=0.5
    x_n2_p1 = xj(j2, n2, p1) # x: n=100 p=0.2
    x_n2_p2 = xj(j2, n2, p2) # x: n= 100 p=0.5

    y_n1_p1 = yj(j1, n1, p1) #y: n = 10 p = 0.2
    y_n1_p2 = yj(j1, n1, p2) #y: n = 10 p = 0.5
    y_n2_p1 = yj(j2, n2, p1) #y: n = 100 p = 0.2
    y_n2_p2 = yj(j2, n2, p2) #y: n = 100 p = 0.5

    g_n1_p1 = guassian(x_n1_p1)
    g_n1_p2 = guassian(x_n1_p2)
    g_n2_p1 = guassian(x_n2_p1)
    g_n2_p2 = guassian(x_n2_p2)

    # plotting two grahs together for readability

    fig, ax = plt.subplots(1, 2)

    ax[0].scatter(x_n1_p1, y_n1_p1,  linewidths=1, color='tab:green',label=fr'binom ($n={n1}, p={p1})$') 
    ax[0].scatter(x_n2_p1, y_n2_p1,  linewidths=1, color='tab:blue', label=fr'binom ($n={n2}, p={p1})$') 
    ax[0].plot(x_n1_p1, g_n1_p1, color='green', label=fr'gauss ($n={n1}, p={p1})$') 
    ax[0].plot(x_n2_p1, g_n2_p1, color='blue', label=fr'gauss ($n={n2}, p={p1})$') 

    ax[0].set_title(fr'$n={n1},{n2};p={p1}$')
    ax[0].legend()

    ax[0].set_xlabel(r'$x$')
    ax[0].set_ylabel(r'$y$')

    ax[1].scatter(x_n1_p2, y_n1_p2, linewidths=1, color='tab:green', label=fr'binom ($n={n1}, p={p2})$')
    ax[1].scatter(x_n2_p2, y_n2_p2, linewidths=1, color='tab:blue',label=fr'binom ($n={n2}, p={p2})$')
    ax[1].plot(x_n1_p2, g_n1_p2, label=fr'gauss ($n={n1}, p={p2})$', color='green')
    ax[1].plot(x_n2_p2, g_n2_p2, label=fr'gauss ($n={n2}, p={p2})$', color='blue')

    ax[1].set_title(fr'$n={n1},{n2};p={p2}$')
    ax[1].legend()


    ax[1].set_xlabel(r'$x$')
    ax[1].set_ylabel(r'$y$')

    plt.show()

main()

"""

The larger the value of n - the better the approximation. It improves when p is near neither 0 or 1.

"""
