#This program is a Rock Paper Scissors Game
import random

rps = ["Rock", "Paper", "Scissors"]
response = 'y'

def welcome_msg():
    print("Welcome to Rock, Paper, Scissors!\n")

def check_response(rep):
    while rep != "y" and rep != "n":
        print("\nInvalid response! Try Again!")
        rep = input("Do you want to play agian? Enter y/n: ")
        return rep

def computer_choice():
    r = random.randint(0,2)
    if r == 0:
        computer = rps[0]
    elif r == 1:
        computer = rps[1]
    else:
        computer = rps[2]
    return computer

def compare_choices(user, computer):
    if user == computer:
        print(f'''Due to both players selecting {user}, It's a tie!''')
    elif user == "Rock":
        if computer == "Scissors":
            print("Rock smashes Scissors. You win!")
        else:
            print("Paper covers Rock. The computer wins!")
    elif user == "Paper":
        if computer == "Rock":
            print("Paper covers Rock. You win!")
        else:
            print("Scissors cut through paper. The computer wins!")
    elif user == "Scissors":
        if computer == "Paper":
            print("Scissors cuts through paper. You win!")
        else:
            print("Rock smashes Scissors. The computer wins!")
    else:
        pass
    

def check_user_choice(c):
    while c != "Rock" and c != "Paper" and c != "Scissors":
        print("You didn't enter a proper value!"
              + "\nPlease try again!")
        c = input("Enter your choice: ")
    return c

def game():
    welcome_msg()
    choice = input("Enter your choice: ")

    user = check_user_choice(choice)
    comp = computer_choice()
    
    compare_choices(user, comp)

def main():
    global response
    while response != 'n':
        game()
        response = input("Do you want to play again? Enter y/n: ")
        check_response(response)
    print("\nThanks for Playing!!")

if __name__ == "__main__":
    main()
