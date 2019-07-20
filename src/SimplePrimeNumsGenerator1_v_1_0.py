'''
#################################################################
    Task:           Creating a simple Primes app

    Description:

                    -   IsPrime(appDefinedNum) function
                        declaration & initialization

                        *   Create a loop starting from 2 up to
                            appDefinedNum

                                *   If loopIndex % 2 == 0

                                    *   return False

                                *   return True

                    -   GetPrime(maxNumber) function
                        declaration & initialization

                        *   Create a list for inserting primes into it

                        *   Create a loop starting from 2 up to
                            maxNumber

                            *   If IsPrime(loopIndex)

                                *   listOfPrimes.append()

                            *   return listOfPrimes


                    userDefinedNumber = int(input("Enter a num: ))

                    userDefinedList = GetPrime(userDefinedNumber)

                    for primeNumber in userDefinedList:

                        print(primeNumber, end=" ")


    Version:        1.0

    Creator:        BugsBunnies1

    Date:           07/20/19
#################################################################
'''

def IsPrime(appDefinedNum):

    for i in range(2, appDefinedNum):

        if (appDefinedNum % i) == 0:

            return False

    return True


def GetPrime(userDefinedNum):

    listOfPrimes = []

    for i in range(2, userDefinedNum):

        if (IsPrime(i)):

            listOfPrimes.append(i)

    return listOfPrimes


def main():

    userDefinedNumber = int(input("Please enter a num: "))

    listOfPrimes = GetPrime(userDefinedNumber)

    for prime in listOfPrimes:

        print(prime, end=" ")

    print("\nThat's all folks... :)")

main()