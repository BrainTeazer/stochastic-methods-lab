import pandas as pd

def main():

    # given values
    P = 500000.0
    balance = P
    r = 0.02
    m = 12 
    n = 20
    
    monthlyInterest = r/m
    totalTime = n * m

    # calculating required monthly payments
    monthlyPayment = monthlyInterest * P * (1 - (1+monthlyInterest) ** (-totalTime)) ** (-1)

    all_data = []
    all_data.append({'Month': 0, 'Principal': 0, 'Interest': 0, 'Balance': balance})
    
    # calcuating principal and interest payment, and remaining balance
    for i in range(1, totalTime + 1):
        month = i
        principalPayment = monthlyPayment - (balance * monthlyInterest)
        interestPayment = balance * monthlyInterest
        balance = monthlyPayment * (1 - (1 + monthlyInterest) ** (-totalTime + i)) / (monthlyInterest) 
        dict1 = {}

        dict1.update({
            'Month': month, 
            'Principal': principalPayment, 
            'Interest': interestPayment, 
            'Balance': balance})

        all_data.append(dict1)

    # adding calucations to panda dataframe
    data = pd.DataFrame(all_data, columns=['Month', 'Principal', 'Interest', 'Balance']).set_index('Month')

    print(data)

main()

