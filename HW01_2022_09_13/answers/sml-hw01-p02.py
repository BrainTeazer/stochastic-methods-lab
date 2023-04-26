import numpy as np

def main():

    # given values
    r = 0.02 # interest rate
    m = 12 # compounded m times per year
    timeDeposit = 480
    timeWithdraw = 360
    x = (1.0 + r/m)
    withdrawAmount = 2000.0

    # PV1 = A * ∑ x^i (i ∈ [1, timeDeposit])
    # PV2 = PV1 * x^max(j) - 2000 ∑ x^j (j ∈ [1, timeWithdraw])
    # PV2 >= 0 
    # PV2 = 0
    # A = ( 2000 / x^max(j) ) * (∑ x^j / ∑ x^i)

    sum1 = np.sum(x ** np.arange(1, timeDeposit+1)) # ∑ x^i (i ∈ [1, timeDeposit])
    sum2 = np.sum(x ** np.arange(1, timeWithdraw+1)) # ∑ x^j (j ∈ [1, timeWithdraw])


    # scrapped idea: f = lambda a : a * sum1 * (x)**(timeWithdraw)  -  withdrawAmount * sum2
    A = (withdrawAmount / (x ** timeWithdraw)) * (sum2/sum1)

    print("A needs to be at least: ", A, "$", sep="")

main()
