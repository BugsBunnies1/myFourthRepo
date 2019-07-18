'''
#################################################################
    Task:           Creating a simple calculator                #
                                                                #
    Description:                                                #
                    -   Demand for user to enter a              #
                        simple equation                         #
                    -   Conversion of types                     #
                    -   A little bit of logic                   #
                    -   Output the result                       #
                                                                #
    Version:        1.0                                         #
                                                                #
    Creator:        BugsBunnies1                                #
                                                                #
    Date:           07/18/19                                    #
#################################################################
'''

# Preprocessor directive
import os

# Demand for user to enter a
# simple equation
myNumOne, myOperator, myNumTwo = input("Please enter simple equation: ").split()

# Conversion of types
myNumOne = float(myNumOne)
myNumTwo = float(myNumTwo)

# A little bit of logic
if myOperator == "+":
    print("You have chosen a math operator of addition, here is the result: {}".format(float(myNumOne + myNumTwo)))
elif myOperator == "-":
    print("You have chosen a math operator of subtraction, here is the result: {}".format(float(myNumOne - myNumTwo)))
elif myOperator == "*":
    print("You have chosen a math operator of multiplication, here is the result: {}".format(float(myNumOne * myNumTwo)))
elif myOperator == "/":
    if myNumTwo == 0:
        print("Sorry, you cannot divide by zero...")
    else:
        print("You have chosen a math operator of division, here is the result: {}".format(float(myNumOne / myNumTwo)))
else:
    print("Please enter a simple math equation..."
          "\nFor example: 20 / 4")