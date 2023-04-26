import numpy as np
import matplotlib.pyplot as plt

# payoff call function
def payoff_call(S, X):
    return np.where(S-X > 0, S-X, 0)

# function to return list to plot butterfly spread
def butterfly_spread(S, args: tuple[float, float, float]):
    X1,X2,X3 = args
    return payoff_call(S,X1) + payoff_call(S,X2)- 2*payoff_call(S,X3)

def main():
    args = (50, 90, 70)
    S = np.linspace(30, 110, 81)

    butterfly = butterfly_spread(S, args)

    plt.plot(S, butterfly)
    plt.xlabel('Stock Price')
    plt.ylabel('Payoff')
    plt.title('Butterfly Spread')
    plt.show()

main()
