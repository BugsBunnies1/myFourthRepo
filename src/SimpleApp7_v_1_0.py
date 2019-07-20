'''
#################################################################
    Task:           Creating a simple Unicode conversion app

    Description:

                    -   Backend interaction:

                        -   Create a variable for storing user defined string


                    -   User interaction:

                        -   Demand for user to enter:

                            * string which will be converted into Unicode

                    -   Backend interaction:

                        -   Create a variable for storing Unicode

                        -   Iterate through every char within user defined string

                            *   Convert user defined string into Unicode

                        -   Create a variable for storing a normal string

                        -   Iterate through newly created string

                            *   Get the 1st and 2nd for the 2 digit number

                            *   Convert the Unicode back to chars

                        -   Output the original string


    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

# Preprocessor directive
import os

# Create a variable for storing user defined string
mySentence = input("Please enter your thoughts: ")

mySentenceChar = ""

# Create a variable for storing Unicode
myUnicode = ""

# Iterate through every char within user defined string
for char in mySentence:
    mySentenceChar += str(ord(char))
print("Secret message: ", mySentenceChar)

# Create a variable for storing a normal string
myNormalString = ""

# Iterate through newly created string
for i in range(0, len(mySentenceChar) - 1, 2):

    # Get the 1st and 2nd for the 2 digit number
    charCode = mySentenceChar[i] + mySentenceChar[i + 1]

    # Convert the Unicode back to chars
    myNormalString += chr(int(charCode))
print("Original message: ", myNormalString)