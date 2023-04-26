import numpy as np 

# brownian paths
def brownian(N,T):
    xi = np.random.normal(loc=0.0, scale=1.0, size=N) * np.sqrt(T/N)

    # conventionally the first element is 0
    xi[0] = 0

    return np.cumsum(xi)


def main():
    # step size 
    step = 1000000

    N = np.arange(step, step * 10, step)

    T = 2

    for num in N:
        Wi = np.square(
                np.diff(brownian(num, T))
            ) 
        print("For {}:\t{}".format(num,np.sum(Wi)))

    print("Clearly the constant that the given expression converges to is T={}.".format(T))
    
main()