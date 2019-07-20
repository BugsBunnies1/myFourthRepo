'''
#################################################################
    Task:           Creating a simple Acronym Generator app

    Description:

                    -   Backend interaction:

                        -   Create a variable for storing user defined string

                    -   User interaction:

                        -   Demand for user to enter a string containing at least two words

                    -   Backend interaction:

                        -   Do the strip procedure

                        -   Capitalize the letters

                        -   Split the words

                        -   Output the acronym


    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

# Preprocessor directive
import os

# Create a variable for storing user defined string
userDefinedString = input("Please enter a string containing at least two words: ")

# Strip left and right spaces
userDefinedString = userDefinedString.lstrip()
userDefinedString = userDefinedString.rstrip()

# Capitalize the letters
userDefinedString = userDefinedString.upper()

# Split the words
userDefinedString = userDefinedString.split()

# Output the acronym:
for word in userDefinedString:
    print(word[0], end="")