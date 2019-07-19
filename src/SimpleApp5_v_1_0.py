'''
#################################################################
    Task:           Creating a simple
                    "return of investment" app

    Description:
                    -   Import a module for digit randomization

                    -   Demand for user to enter:

                            * a number which only he/she knows

                    -   Conversion of types

                    -   Logic has to guess user defined number

                    -   Output the result of guessed number

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/19/19
#################################################################
'''

# Preprocessor directive
import os
import random

# number which only user knows
userDefinedNumber = (input("Please enter a digit (1 - 10): "))

# Conversion of types
userDefinedNumber = int(userDefinedNumber)

# Guess user defined number
guessNumber = random.randrange(1, 10)
while guessNumber != userDefinedNumber:
    guessNumber = random.randrange(1, 10)
    print("Digit randomization logic has chosen number {}".format(guessNumber))
    print()
    if guessNumber == userDefinedNumber:
        # Output the result of guessed number
        print("Yeap, we've found your number: {}".format(guessNumber))

