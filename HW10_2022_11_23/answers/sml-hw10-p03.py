import numpy as np
from scipy.stats import norm


def bsExplicit(X, S,K,T, N, M, r,sigma):
    # boundary conditions 
    V_x0_t = np.zeros(M) # all time thingys
    V_xmax_t = 1
    V_x_t = 2

    dt = 1/M
    x = np.linspace(-X, X, N+1)
    dX = (2 * X) / N
    S = np.exp(x)
    S_max = np.exp(X)

    #V^m_n = V^m_(n-1) + 
    V_m_n = np.zeros((N+1, M))
    a = 1 - dt * ((sigma * sigma) / (dX*dX) + r) # for V^(m)_n
    b = dt * (sigma ** 2 / (2 * dX ** 2) - (r - sigma ** 2 / 2) / (2 * dX)) # for V^(m)_(n-1)
    c = dt * (sigma ** 2 / (2 * dX ** 2) + (r - sigma ** 2 / 2) / (2 * dX))# for V^(m)_(n+1)

    return V_m_n
    
    
def bsImplicit(S,K,T, N, M, r,sigma):
    print("test")

def blackScholes(S, K, T, r, sigma):
    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))
    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))

def main():
    X = 4
    S = 1
    K = 0.7
    r = 0.01
    sigma = 0.1
    T = 1 
    

    print('L');

main()
