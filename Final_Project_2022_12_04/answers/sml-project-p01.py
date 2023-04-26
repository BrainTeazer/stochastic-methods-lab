import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm
import matplotlib.pyplot as plt 
from datetime import datetime 

FILE = "SPOT-RATE-DATA_US.csv"

# black scholes
def blackScholes(S, K, T, r, sigma):
    """! Get option using black scholes formula

    @param S        Stock price.
    @param K        Strike price.
    @param T        Time to maturity (in years)
    @param r        Risk-free interest rate (in decimal)
    @param sigma    Volatility.

    @return         Option price.
    """

    x = (np.log(S/K) + (r + (sigma * sigma) / 2. )/T) / (sigma * np.sqrt(T))

    return S * norm.cdf(x) - K * np.exp ( -r * T ) * norm.cdf(x - sigma * np.sqrt(T))


def deltaDays(date, dateFormat):
    """! Get number of days between today and provided date

    @param date             Number of days between today's date and this parameter
    @param dateFormat       Format of the date 
   
    @return                 Number of days between today and provided price.
    """

    return np.abs(datetime.now() - datetime.strptime(date, dateFormat)).days

def logReturn(S):
    """! Get the log return of stock price and the standard deviation

    @param S    Array of stock prices.
   
    @return     An array of log returns and the approximate sigma.
    """

    # The data found is for each trading day thoughout the year - and the total number of trading days is 252 (https://en.wikipedia.org/wiki/Trading_day)
    # So the dt = 1/252
    dt = 1/252
    stLogReturn = np.diff(np.log(S))
    var = np.var(stLogReturn)
    aS = np.sqrt(var / dt) # approx Std

    return stLogReturn, aS

# get the rates for 
def interpolateFromFile(FILE):
    """! Get maturity dates and interest rate of each

    @param FILE    Filename to get the data
   
    @return     Two arrays - first containing time to maturity dates and second containing its corresponding risk free rate.
    """
    
    data = pd.read_csv(FILE)
    dates = []
    rates = []

    spotRates = data.iloc[0] # get the first row 

    for index, spotRate in enumerate(spotRates[1:]):
        dates.append(index+1)
        rates.append(spotRate)

    return dates, rates



# from assignment 5
def X(J):
    return (J - np.mean(J))/np.std(J)


def main():
    # non-dividend paying stock; however, American options are used.
    # European options tend to pay dividends, and o not have option data that is easily accessible  
    # According to Lyuu (Chapter 9.2), American call options exercised early are not optimal - so,
    # it can be used instead of European call option which are exercised always at the end. 
    name = 'AMZN'
    company = yf.Ticker(name) 
    dateFormat = "%Y-%m-%d"


    # dates of Maturity
    dateList = ["2023-10-20", "2025-01-17"]

   
    # getting stock price
    STOCK_FILE = name+'-stock-data.csv'
   
    """ Uncomment to get data from online and store it in a file
    
    companyStock = company.history(period='max')['Close']
    pd.DataFrame(stockData).to_csv(STOCK_FILE)
    
    """

    companyStock = np.array(pd.read_csv(STOCK_FILE)['Close'])


    stLogReturn, aS = logReturn(companyStock)

    normDLogRet = np.random.normal(loc=0.0, scale=1.0, size=len(stLogReturn))
    normDist = np.sort(X(normDLogRet))
    st = np.sort(X(stLogReturn))


    plt.plot(normDist, normDist, label="Normal Distribution")
    plt.scatter(normDist, st, s=3, label="QQ-Plot")
    plt.title("QQ-Plot")
    plt.xlabel("Normal Distribution")
    plt.ylabel("Log return")
    plt.plot()

        
    plt.figure()
    plt.acorr(stLogReturn, label="Autocorrelation")
    plt.title("Autocorrelation Function")
    plt.xlabel("Autocorrelation")
    plt.ylabel("Log Returns")
    plt.legend()

    # From the QQ-plot we can see that at the tail-ends of the plot, it seems to deviate/diverge from the normal distribution
    # but matches it relatively well in the middle. 
    # As for the autocorrelation, it is mostly 0 throughout the graph, showcasing independence to preceding data points.

    dates, rates = interpolateFromFile(FILE)

    # the date this was executed is 2022-12-23
    # Time periods is respect to a year
    timePeriods = [deltaDays(date, dateFormat)/365 for date in dateList]
    rs = [np.interp(period, dates, rates) for period in timePeriods]

    companyCalls = []
    for date in dateList:
        OPTION_FILE = name+'-option-'+date+'.csv'

        """ Uncomment to get call option data online and store in file 
        
        companyCall = company.option_chain(date).calls 
        pd.DataFrame(companyCall).to_csv(OPTION_FILE)

        """
        companyCalls.append(pd.read_csv(OPTION_FILE))


    _, ax = plt.subplots(1, len(companyCalls))

    for i in np.arange(len(companyCalls)):
        companyOptions = companyCalls[i]["lastPrice"]
        companyStrike = companyCalls[i]["strike"]
        bS = [blackScholes(companyStock[-1], strike, timePeriods[i], rs[i]/100, aS) for strike in companyStrike]
        ax[i].plot(companyStrike, bS, label="Black Scholes")
        ax[i].set_xlabel("Strike Price")
        ax[i].set_ylabel("Option Price")
        ax[i].set_title(f"Comparison between Black Scholes and Actual. T={timePeriods[i]}")
        ax[i].plot(companyStrike, companyOptions, label="Actual")
        ax[i].legend()

    # The Black Scholes is over estimating the actual price. This may be due to it 
    # assuming various factors like a constant risk free interest rate and ignoring others 
    # like a changes in volatility, which leads to an overestimation of the actual price.

    # With an increase in time to maturity and strike price the estimation seems to worsen. 
    # Which again may be due to the fact that black scholes ignores many factors and creates 
    # assumptions about other factors.
    


    plt.show()


main()

"""

Source for U.S. Zero-Coupon Yield Curve: https://data.nasdaq.com/data/FED/SVENY-us-treasury-zerocoupon-yield-curve

In homework 8, it was mentioned "The applicable interest rate is the spot rate for zero coupon bonds of the same maturity"
which is equivalent to the zero-coupon yield curve

"""



"""
(d)

The methods for finding options prices discussed in class are:
    1. Monte Carlo
        a) Advantages (https://sars.org.uk/BOK/Applied%20R&M%20Manual%20for%20Defence%20Systems%20(GR-77)/p4c04.pdf): 
            - Easily understandable 
            - Very flexible 
            - As per person's needs, it can be extended and developed 
        b) Disadvantages:
            - Computation requirements can be very high (https://jameshoward.us/2019/09/07/monte-carlo-simulation-advantages-and-disadvantages/)
            - All outputs are estimates, and depends greatly on the number of the iterations (https://sars.org.uk/BOK/Applied%20R&M%20Manual%20for%20Defence%20Systems%20(GR-77)/p4c04.pdf) 
    
    2. Binomial Tree (https://www.linkedin.com/pulse/option-pricing-black-scholes-v-binomial-monte-carlo-stringham)
        a) Advantages:
            - With large iterations, it converges with Black Scholes
            - Offers for more flexibility at each step compared to Black Scholes
        b) Disadvantages
            - Slow computations and complex

    4. Black-Scholes
        a) Advantages (https://www.letslearnfinance.com/black-scholes-model-advantages-and-disadvantages.html):
            - It is highly accurate 
            - Due to the use of a mathematical formula, it is very quick in pricing options
        b) Disadvantages:
            - Cannot be used for American option styles
            - It makes assumptions (like no arbritage opportunities) and ignores various other factors (like changes in volatility)
                (https://www.letslearnfinance.com/black-scholes-model-advantages-and-disadvantages.html)

    5. Finite Difference
        a) Advantages:
            - Simplicity, and ease of high-order approximations and computation due to use of Banded Matrix approximation
            - Various schemes, with a variety of yields
        b) Disadvantages
            - Due to requirement of boundary conditions, applications can be limited 

"""
