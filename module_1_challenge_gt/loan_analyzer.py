# coding: utf-8
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

#prints the number of loans in the loan_costs list. 
print(f'The number of loans is {len(loan_costs)}.')

#prints the sum (total cost) of the loans in the loan_costs list
print(f'The total value of the loans is {sum(loan_costs)}.')

#calculates the arithmetic mean (average) cost of a loan in the list loan_costs
print(f'The average loan amount is {sum(loan_costs)/len(loan_costs)}.')

################################# Part 2 #################################
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#pulls and prints necessary individual values related to keys in the dictionary "loan" 
#saves these values as variables for use in calculating present value of the loan
futval = loan.get('future_value')
print(futval)
remmon = loan.get('remaining_months')
print(remmon)
loanprice = loan.get('loan_price')
print(loanprice)

#discount rate: 20%
disrat = 0.2

#calculates present value of the loan using the present value formula
#saves the result in the presval variable
presval = futval / (1 + disrat/12 ) **remmon

#checks to see if the present value of the loan is less than or equal to the price of the loan
#prints whether or not the loan is worth purchasing. worth it if present value < loan price
# present value rounded to 2 decimal places 
if presval >= loanprice:
    print(f'The present value of the loan is {round(presval, 2)}. \n The loan is worth at least the cost to buy it. \n It makes sense to buy this loan.')
else: 
    print('The loan is too expensive and not worth the price.')

################################# Part 3 #################################

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#pulls individual values related to the keys in the dictionary "new_loan"
future_value = new_loan.get('future_value')
remaining_months = new_loan.get('remaining_months')
annual_discount_rate = .20 

#defines a function that caluclates the present value of a loan using the present value formula
def presentvalue(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/(1 + annual_discount_rate/12)**remaining_months
    return(present_value)

#calls the presentvalue function 
final_value = presentvalue(future_value, remaining_months, annual_discount_rate)

#prints the result of calling the presentvalue function, rounded to 2 decimal places
print(f"The present value of the loan is: {round(final_value, 2)}.")

################################# Part 4 #################################

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Empty list. Results of code below (for statement) appended to this list
inexpensive_loans = []


#loops through the dictionaries in the list "loans"
#checks to see if the price of the loan ("loan_price") is less than or equal to 500
#adds the dictionary containing a loan price < or = 500 to inexpensive_loans list
for loan in loans:
    if loan['loan_price'] <= 500: 
        inexpensive_loans.append(loan)
    else:
        continue

#prints the list of inexpensive loans 
print(inexpensive_loans)

################################# Part 5 #################################

#header of the chart of loans to be saved to csv file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#output saved to inexpensive_loans.csv
output_path = Path("inexpensive_loans.csv")

#sets up csv file to be written to 
#adds header to csv file
#adds inexspensive_loans list, values of dictionaries to csv file, each value in its own cell under appropriate heading
#each loan in its own row 
with open(output_path, 'w') as csvfile: 
    csvwriter= csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for indiv_loan in inexpensive_loans:
        csvwriter.writerow(indiv_loan.values())
    
