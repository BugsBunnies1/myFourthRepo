'''
#################################################################
    Task:           Creating a simple app for calculating
                    area of different types of math shapes

    Description:

                    -   Import a math module

                    -   Design AreaRectangle(userDefinedHeight, userDefinedWidth)

                    -   Design AreaCircle(userDefinedRadius)

                    -   Design UserPreference(decision)

                    -   Design main()

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

import math


def AreaRectangle():

    height = float(input("Please enter height: "))

    width = float(input("Please enter width: "))

    return height * width


def AreaCircle():

    radius = float(input("Please enter radius: "))

    return (math.pi * (math.pow(radius, 2)))

def UserPreference(decision):

    decision = decision.lower()

    if decision == "rectangle":

        return AreaRectangle()

    elif decision == "circle":

        return AreaCircle()

    else:
        print("Please enter either rectangle or circle...")


def main():

    userPreference = input("Please enter math shape for calculating the Area (rectangle or circle): ")

    print("Area: ",UserPreference(userPreference))


main()