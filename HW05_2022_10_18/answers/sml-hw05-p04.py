import numpy as np
import matplotlib.pyplot as plt

# X
def X(J):
    return (J - np.mean(J))/np.std(J) 

def main():
    N = 10000
    p = 0.2

    binom = np.sort(X(np.random.binomial(N,p, N)))
    normal = np.sort(X(np.random.normal(N,p, N)))

    plt.plot(normal, normal, label='Diagonal')
    plt.scatter(normal, binom, linewidth=1, color='g', label='QQ-Plot')

    plt.title('Normal vs Binomial Distribution')

    plt.xlabel('Normal Distribution')
    plt.ylabel('Binomial Distribution')

    plt.legend()

    plt.show()

main()

"""
We can see that the binomail distribution is approximately normally distributed (i.e. the central limit theorem). N=10000 is a large sample - and as the samples get larger the two distributions get to be approximately equal.

"""
