'''
#################################################################
    Task:           Creating a simple exception handling app

    Description:

                    -   Backend interaction:

                        -   Create a variable for storing user defined number


                    -   User interaction:

                        -   Demand for user to enter:

                            * a number


                    -   Backend interaction:

                        -   Conversion of types

                            *   Convert user defined height

                        -   Exception handling

                            *   If user typed alpha instead of a number

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

# Preprocessor directive
import os

# Create a loop
while True:

    # Exception handling procedure if user entered alpha instead of a number
    try:

        # Create a variable for storing user defined number
        myNumber = int(input("Please enter a random number: "))
        break

    except ValueError:

        print("Error: you haven't entered a number..."
              "\nPlease try again:\n\n")

    except:

        print("An unknown error occurred...")

print("Thanks for entering a num... :)")
