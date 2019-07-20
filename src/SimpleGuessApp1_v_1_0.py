'''
#################################################################
    Task:           Creating a simple guess app

    Description:

                    -   Backend interaction:

                        -   Create a variable for storing user defined number


                    -   User interaction:

                        -   Demand for user to enter:

                            * a number which has to be guessed


                    -   Backend interaction:

                        -   Conversion of types

                            *   Convert user defined number

                        -   Create "do keep on guessing while you haven't found the number" loop

                        -   Exception handling

                            *   If user typed alpha instead of a number

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

# Preprocessor directive
import os
import random

# Test exception handling
while True:

    try:
        # Create a variable for user defined number
        userDefinedNumber = int(input("Please enter random number: (1 - 10)"))
        break

    except ValueError:
        print("You haven't entered a number...")

    except:
        print("Unknown error appeared...")
print("Thanks for entering a number... :)")

# Create a random number generator
randomNumberGenerator = random.randrange(1, 10)

# Create a guess number variable
myGuess = 0
myGuess = int(myGuess)

# Create a a loop
while(myGuess != userDefinedNumber):

    # Create a bunch of random numbers
    randomNumberGenerator = random.randrange(1, 10)
    myGuess = randomNumberGenerator
    print(myGuess)

print("You have guessed the number!!!")