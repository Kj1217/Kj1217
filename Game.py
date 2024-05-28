#This program will generate a random number and the user has to guess it
import random


def congrats():
    print("Congrats! You've guessed the correct number!")

def generate_Number():
    r = random.randint(0, 100)

    return r

def compareNum(uNum, r):
    while uNum != r:
        if uNum > r:
            print("Your number is higher than the target value!")
        else:
            print("Your number is lower than the target value!")

        uNum = int(input("Enter another number: "))
        checkUserNum(uNum)

    congrats() 

def checkUserNum(num):
    while not(num >= 1 and num < 100):
        print("Your number isn't in the range")
        print("Try again!")

        num = int(input(f'Enter a number between 1 and 100: '))
        
    return num    

def main():
    print("Welcome to the Random Number Generator!")
    print("----------------------------------------")
    print("\nThis program will generate a random number\nbetween a range"
          + " of 1 and 100 and you have to guess it.")
    response = "Y"

    while response != "N":

        r = generate_Number()
        userNum = int(input("\nEnter a number: "))

        uNum = checkUserNum(userNum)

        compareNum(uNum, r)

        response = str(input("Do you want to try again? Enter Y/N: "))
    print("Thanks for playing!")    
    

if __name__ == "__main__":
    main()
