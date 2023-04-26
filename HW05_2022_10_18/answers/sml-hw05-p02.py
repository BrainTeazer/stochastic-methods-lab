from scipy import special
import numpy as np
import matplotlib.pyplot as plt

def stirlingApprox(n):
    return np.sqrt(2 * np.pi * n) * np.power(n/np.exp(1), n)

def factorial(n):
    return special.factorial(n)


def main():
    n = np.arange(1, 101)

    stirling = stirlingApprox(n)
    relativeError = np.absolute((factorial(n) - stirling)) / stirling

    plt.loglog(n, relativeError)
    plt.title('LogLog plot of rel. error (Stirling approx.)')
    plt.xlabel(r'$n$ in $log$ scale')
    plt.ylabel(r'rel. error in $log$ scale')

    slope = np.polyfit(np.log(n), np.log(relativeError), 1)[0]
    print("Slope is {}".format(slope))

    plt.show()

main()

"""

Because the slope of the plotted graph is approximately -1 - the error is proportional to 1/n.
Therefore, the next order of the approximation is approximately O(1/n)

"""
