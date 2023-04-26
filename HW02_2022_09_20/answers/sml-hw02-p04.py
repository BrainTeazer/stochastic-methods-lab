import matplotlib.pyplot as plt
import numpy as np

def P(r, F, c, n, m):
    C = F * c / m
    i = np.arange(1, n*m+1)
    return F * (c/r + (1 - c/r)/(1+r/m) ** (n*m) )

def main():
    n = 10
    m = 1
    c = 0.08
    F = 1000.0
    yields = np.linspace(0.0, 1.0, 10000)
    prices = []

    for r in yields:
        prices.append(P(r, F, c, n, m))
    plt.plot(yields*100, prices)

    plt.xlabel('Yield to Maturity (%)')
    plt.ylabel('Price of the bond')
    plt.title('Price of bond vs. YTM')

    plt.show()

main()
