import matplotlib.pyplot as plt
import numpy as np

# Assuming Coupon Rate is 0
def FV(rold, rnew, F, m, n, h): 
    return F * ((1+rnew/m) ** (m*h)) / ((1 + rold/m)**(n*m))

def main():
    F = 1
    m = 2
    h = 15

    rold = 0.08
    ytm = np.arange(1, h*2)

    intRates = [0.06, 0.08, 0.10]

    for r in intRates: 
        y = [FV(rold, r, F, m ,n, h) for n in ytm]
        plt.plot(ytm, y, label="r={}%".format(r*100))

    plt.xlabel('Years to Maturity')
    plt.ylabel('Forward Value')
    plt.title('Forward Value vs. YTM')
    plt.legend()

    plt.show()


main()
