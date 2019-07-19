'''
#################################################################
    Task:           Creating a simple drawing of a PineTree

    Description:

                    -   Backend interaction:

                        -   Create a variable for storing user defined height


                    -   User interaction:

                        -   Demand for user to enter:

                            * a number which is going to represent height of the tree


                    -   Backend interaction:

                        -   Conversion of types

                            *   Convert user defined height

                        -   Create a variable which stores current height of the tree

                        -   Create a variable which stores current number of symbolic PineTree signs

                        -   Create a variable which stores current number of spaces

                        -   Create a variable which stores stump position

                        -   Create a loop

                            *   While the current height of the tree is not equal to the user defined height
                                (OR: WHILE THE CURRENT NUMBER OF SPACES IS NOT EQUAL TO ZERO)


                                        *   Output the result of the current number of spaces

                                        *   Output the result of the current number of symbolic PineTree signs

                                        *   Decrement the current number of spaces by one

                                        *   Increment the current number of symbolic PinTree signs by two

                                        *   Increment the current height of the tree

                                            *   If current number of spaces is equal to zero

                                                *   Output the stamp of the PineTree

    Example:
                    #
                   ###
                  #####
                 #######
                    #

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/19/19
#################################################################
'''

# Preprocessor directive
import os

# Create a variable which stores user defined height
myPineTreeHeight = input("Please enter a num which is going to represent the height of the PineTree: ")

# Convert user defined height
myPineTreeHeight = int(myPineTreeHeight)

# Create a variable which stores current height of the tree
myPineTreeCurrentHeight = 0

# Create a variable which stores current number of symbolic PineTree signs
myPineTreeSigns = 1

# Create a variable which stores current number of spaces
myPineTreeSpaces = myPineTreeHeight - 1

# Create a variable which stores stump position
myPineTreeStump = myPineTreeHeight - 1

# Create a loop
while myPineTreeCurrentHeight != myPineTreeHeight:
    print(" " * myPineTreeSpaces, end="")
    print("#" * myPineTreeSigns)
    #print()
    myPineTreeSpaces -= 1
    myPineTreeSigns += 2
    myPineTreeCurrentHeight += 1
    if myPineTreeCurrentHeight == myPineTreeHeight:
        for i in range(myPineTreeStump):
            print(" ", end="")
        print("#")