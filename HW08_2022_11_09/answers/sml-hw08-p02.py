import numpy as np
import matplotlib.pyplot as plt
from yahoo_fin.options import *

def blackScholes(S, K, T, r, sigma):
    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))

    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))

def main():
    T = 1 
    
    ntflx_exp_date = get_expiration_dates("nflx")
    
    info ={}
    
    for date in ntflx_exp_date:
        info[date] = get_calls("nflx")

    print(info["January 20, 2023"])


main()
