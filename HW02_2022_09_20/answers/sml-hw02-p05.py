import numpy as np
import matplotlib.pyplot as plt


def priceVolatility(F, y, c, n, m):
    C = F * c / m

    # formula given in the book with y = r/m
    return -\
            ((C/y)*(n*m) - (C / y ** 2.0) * ((1.0+y) ** ((n*m)+1.0) - (1.0+y)) - (n*m) *F)\
            / ((C/y)*( (1.0+y)**((n*m)+1.0) - (1.0+y)) + F*(1.0+y))


def main():
    coupons = [0.02, 0.06, 0.12]
    r = 0.06
    m = 2
    y = r/m
    F = 1000
    times = np.arange(0, 101)


    volatilities = []

    for coupon in coupons:
        volatilities = [priceVolatility(F, y, coupon, time, m) for time in times]
        plt.plot(times, volatilities, label='c = {}%'.format(coupon * 100))

    plt.xlabel('Time to Maturity (in years)')
    plt.ylabel('Price volatility')
    plt.title('Price volatility vs. Time to Maturity')
    plt.legend()
    plt.show()

main()

    

