'''
#################################################################
    Task:           Creating a simple app                       #
                                                                #
    Description:                                                #
                    -   Demand for user to enter two values     #
                    -   Conversion of types                     #
                    -   Output result of basic math operations  #
                        onto those two values                   #
                                                                #
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

# Demand for user to enter two values
# numOne = input("Please enter random number: ")
# numTwo = input("Please enter another one: ")
numOne, numTwo = input("Please enter two random numbers: ".split())

# Conversion of types
numOne = int(numOne)
numTwo = int(numTwo)

# Output result of basic math operations
# onto those two values

print("Summation of {} and {} is:\t\t{}".format(numOne, numTwo, numOne + numTwo))
print("Subtraction of {} and {} is:\t\t{}".format(numOne, numTwo, numOne - numTwo))
print("Multiplication of {} and {} is:\t{}".format(numOne, numTwo, numOne * numTwo))
print("Division of {} and {} is:\t\t{}".format(numOne, numTwo, numOne / numTwo))

