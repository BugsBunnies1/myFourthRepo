'''
#################################################################
    Task:           Creating a simple Ceasar Cypher app

    Description:

                    -   Backend interaction:

                        -   Create a variable for a message that
                            needs to be encrypted

                        -   Create a variable for a number of
                            character shift right-s

                    -   User interaction:

                        -   Demand for user to enter a message

                        -   Demand for user to enter a number

                    -   Backend interaction:

                        -   Message strip

                        -   Conversion of types

                            *   Convert user defined number

                        -   Create a variable for storing a secret message

                        -   Output the original message

                        -   Output the character shift variable

                        -   Output the encrypted message


    Example:
                    userDefinedString = "Start the battle"

                    userDefinedNumber = 3

                    secretMessage     = "Vwduw wkh edwwoh"

    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

# Create a variable for a message that needs to be encrypted
myMessage = input("Please enter a message: ")

# Strip the message
myMessage = myMessage.lstrip()
myMessage = myMessage.rstrip()

# Create a variable for a number of character shift right-s
myCharShift = int(input("Please enter a number of char shifts that will be done: "))

# Create a variable for a message that has been encrypted
mySecret = ""

# Logic!!!
for char in myMessage:

    if char.isalpha():

        unicodeChar = ord(char)
        unicodeChar += myCharShift

        if(char.islower()):

            if unicodeChar > ord('z'):
                unicodeChar -= 26

            if unicodeChar < ord('a'):
                unicodeChar += 26

            print("Char is lower:\t", char)
            print("New unicode:\t", unicodeChar)
            newChar = chr(int(unicodeChar))
            print("New char:\t\t", newChar)
            print("********************")

        else:

            if unicodeChar > ord('Z'):
                unicodeChar -= 26

            if unicodeChar < ord('A'):
                unicodeChar += 26

            print("Char is upper:\t", char)
            print("New unicode:\t", unicodeChar)
            newChar = chr(int(unicodeChar))
            print("New char:\t\t", newChar)
            print("********************")

        mySecret += chr(unicodeChar)

# Output the original message
print("Original message: ", myMessage)

# Output the character shift variable
print("How many times of char shifting on each char: ", myCharShift)

# Output the encrypted message
print("My secret message: ", mySecret)