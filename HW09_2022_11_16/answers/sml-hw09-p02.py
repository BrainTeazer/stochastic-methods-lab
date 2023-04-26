import numpy as np
import matplotlib.colors as mc
import matplotlib.pyplot as plt

# payoff function
def payoff(S, K, opt='C'):
    if opt.upper() == 'C':
        return np.maximum(S-K, 0)
    elif opt.upper() == 'P':
        return np.maximum(K-S, 0)

# binomial tree european
def binomial_tree(payoff, n, rp, sigma, S, K, T):
    tt = T/n
    u = np.exp(sigma * np.sqrt(tt))
    d = 1 / u

    q = (np.exp(rp * tt) - d) / (u-d)

    S1 = S * d ** (np.arange(n, -1, -1)) * u ** (np.arange(0, n+1, 1))
    poff = payoff(S1, K)

    # storing the option value at each node of the treee
    nodes = [(poff := np.exp(-rp * tt) * (q * poff[1:i+1] + (1-q) * poff[0:i]) ) for i in np.arange(n,0,-1)]

    return nodes

def getMasked(nodes):

    # get the longest node
    maxLen = len(max(nodes, key=len))
    masks = []
    allNodes = []

    # adding masks/padding to each node of the tree equal the length of the longest node 
    for node in nodes:

        # adding equal padding to top and bottom of node
        nodeLen = len(node)
        lenDiff = maxLen - nodeLen
        
        halfDiff = int(np.ceil(lenDiff/2))

        back = np.zeros(halfDiff)
        front = np.zeros(lenDiff - halfDiff)
        
        allNodes.append(np.concatenate([front, node, back]))

        # creating a corresponding mask with added padding being invalid (1)
        masks.append(np.concatenate([np.ones(len(front)), np.zeros(nodeLen), np.ones(len(back))]))
                        
                        
    return allNodes, masks


def main():
    # using the value given in HW04 p02
    S = 1
    K = 0.7
    rp = 0.02
    T = 1
    n = 1000
    sigma = 0.5

    # getting the nodes
    tree = binomial_tree(payoff, n, rp, sigma, S, K, T)
    tree.reverse() # so that first element is the price of the option at T=0

    # getting masked array
    nodes, masks = getMasked(tree)
    
    
    X = np.ma.masked_array(nodes, masks)
    X = np.flip(X.T, axis=0) # transpose and flip to get graph to the left

    plt.imshow(X, cmap="Dark2", norm=mc.PowerNorm(0.125)) # aesthetics
    plt.show()

main()
