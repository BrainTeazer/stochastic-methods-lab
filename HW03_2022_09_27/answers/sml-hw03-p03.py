import numpy as np
import matplotlib.pyplot as plt

# payoff call function
def payoff_call(S, X):
    return np.where(S-X > 0, S-X, 0)

# payoff put function
def payoff_put(S, X):
    return np.where(X-S > 0, X-S, 0)

def main():
    X = 100
    S = np.linspace(0, 200, 100)

    call = payoff_call(S, X)
    put = payoff_put(S, X)


    plt.plot(S, call, label='Payoff for a European call option')
    plt.plot(S, put, label='Payoff for a European put option')
    plt.xlabel('Stock Price')
    plt.ylabel('Payoff')
    plt.title('Stock vs Payoff (Strike Price = $100)')
    plt.legend()
    plt.show()



main()
