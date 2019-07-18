'''
#################################################################
    Task:           Creating a simple app                       #
                                                                #
    Description:                                                #
                    -   Demand for user to enter a value        #
                        (in miles)                              #
                    -   Conversion of types                     #
                    -   Output the result                       #
                        (in km)                                 #
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

# Demand for user to enter a value
# (in miles)
userValueMiles = input("Please enter a value (in miles): ")

# Conversion of types
userValueMiles = float(userValueMiles)
userValueKm = userValueMiles * 1.609344

# Output the result
# (in km)
print("{:.2f} in miles is {:.2f} in kilometers...".format(userValueMiles, userValueKm))