import numpy as np
import matplotlib.pyplot as plt

# binomial tree european
def binomial_tree_european(payoff, n, rp, sigma, S, K, T = 0, opt='C'):
    tt = T/n
    u = np.exp(sigma * np.sqrt(tt))
    d = 1 / u

    q = (np.exp(rp * tt) - d) / (u-d)

    S1 = S * d ** (np.arange(n, -1, -1)) * u ** (np.arange(0, n+1, 1))
    poff = payoff(S1, K, opt)

    for i in np.arange(n, 0, -1):
        poff = np.exp(-rp * tt) * (q * poff[1:i+1] + (1-q) * poff[0:i])

    return poff[0]

# binomial tree american
def binomial_tree_american(payoff, n, rp, sigma, S, K, T = 0, opt='C'):
    u = np.exp(sigma * np.sqrt(T/n))
    d = 1 / u

    R = np.exp(rp*(T/n))

    p = (R-d)/(u-d)

    S1 = S * d ** (np.arange(0, n+1, 1)) * u ** (np.arange(n,-1, -1))
    poff = payoff(S1, K, opt)

    for j in np.arange(n-1, -1, -1):

        S2 = S * u ** np.arange(j, -1, -1) * d ** np.arange(0, j+1,1)
        m1 = p * poff[0:j+1] + (1-p)* poff[1:j+2]

        if opt == 'P':
            poff = np.maximum(m1/R, K - S2)
        elif opt == 'C':
            poff = np.maximum(m1/R, S2-K)

    return poff[0]

# payoff function (put and call)
def payoff(S, K, opt='C'):
    if opt.upper() == 'C':
        return np.maximum(S-K, 0)
    elif opt.upper() == 'P':
        return np.maximum(K-S, 0)

def main():
    S = 1
    K = np.linspace(0,2, 30)
    rp = 0.02
    T = 1
    n = 1000
    sigma = 0.5

    put_america = [binomial_tree_american(payoff,n,rp,sigma,S,strike,T,'P') for strike in K]
    put_europe = [binomial_tree_european(payoff,n,rp,sigma,S,strike,T,'P') for strike in K]

    print("American Call Value (Strike Price = {}): {}".format(0.7, binomial_tree_american(payoff, n, rp, sigma, S, 0.7, T, opt='C')))
    print("American Put Value (Strike Price = {}): {}".format(90, binomial_tree_american(payoff, n, rp, sigma, S, 0.7, T, opt='P')))

    # check if american put > european put
    if (put_america > put_europe):
        answerTxt = "American put $>$ European put\n(Identical Parameters)"
    else:
        answerTxt = r"American put $\leq$ European put\n(Identical Parameters)"


    # plotting values
    plt.plot(K, put_america, label='American Put')
    plt.plot(K, put_europe, label='European Put', linestyle='dashed')

    parameterTxt = "\n".join((
        r'$\sigma=%.3f$' % (sigma, ),
        r'$S=%.3f$' % (S, ),
        r'$T=%.3f$' % (T, ),
        r'$n=%d$' % (n, ),
        r'$r_p=%.4f$' % (rp, ),
        ))
    
    boxProp = dict(facecolor='none', edgecolor='gray')

    plt.text(K[0]+0.43, 0.8,answerTxt,verticalalignment='center', horizontalalignment='center', bbox=boxProp)
    plt.text(K[-1]-0.15,0.2,parameterTxt,verticalalignment='center', horizontalalignment='center', bbox=boxProp)

    plt.xlabel('Strike Price ($)')
    plt.ylabel('Put')
    plt.title('American Put vs. European Put (Varying Strike Price)')
    plt.legend()
    plt.show()

main()

