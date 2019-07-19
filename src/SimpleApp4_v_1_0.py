'''
#################################################################
    Task:           Creating a simple
                    "return of investment" app

    Description:
                    -   Demand for user to enter:

                            * amount of money invested
                            * interest rate

                    -   Conversion of types

                    -   Calculate earnings (1 year lifespan)

                    -   Calculate earnings (10 year lifespan)

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/19/19
#################################################################
'''


# Preprocessor directive
import os

# Amount of money invested
myMoney = input("Please enter money that you want to invest: ")

# Amount of interest rate
myInterestRate = input("Please enter interest rate: ")

# Conversion of types
myMoney = float(myMoney)
myInterestRate = float(myInterestRate) * .01

# Calculate earnings (10 year lifespan)
for year in range(10):
    myMoney = myMoney + (myMoney * myInterestRate)

# Output the result
print("Interest after 10 years: {:.2f}".format(myMoney))