import matplotlib.pyplot as plt
import numpy as np 

def P(r, F, c, n, m):
    C = F * c / m

    return F * (c/r + (1 - c/r)/(1+r/m) ** (n*m) )

def main():
    coupons = [0.02, 0.06, 0.12]
    m = 2
    F = 1000
    r = 0.06
    n = np.linspace(0, 100, 10000)
    m = 2

    for coupon in coupons:
        y = P(r, F, coupon, n, m)
        plt.plot(n, y, label='c = {}%'.format(coupon * 100))

    plt.xlabel('Time to maturity (in years)')
    plt.ylabel('Price')
    plt.title('Price vs. Time to maturity')

    plt.legend()
    plt.show()

main()
