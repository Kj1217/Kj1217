
def message():
    print("\tQuiz Game")
    print("This program will ask you 10 very random\nquestions" +
      "  on certain topics and will then display your score.")
    
    name = input("Enter your name: ")
    print(f'\nWelcome {name}!')
    return name

def questions():
    points = 0

    answer = input("\nQuestion 1: What does UML stand for?\nAnswer: ")
    if answer == "Unified Modeling Language":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is Unified Modeling Language")

    answer2 = input("\nQuestion 2: What is the abbreviation for Virtual Private Network?\nAnswer: ")
    if answer2 == "VPN":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is VPN")
    
    answer3 = input("\nQuestion 3: Which of the following isn't an input device?\n" +
                    "A. Mouse\nB. Keyboard\nC. Xbox Controller\nD. Monitor\nAnswer: ")
    if answer3 == "D":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer was D. Monitor")

    answer4 = input("\nQuestion 4: What part of the computer is known as the brain?\n" +
                    "A. GPU\nB. CPU\nC. Motherboard\nD. PSU\nAnswer: ")
    if answer4 == "B":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\n The correct answer is B. CPU")

    answer5 = input("\nQuestion 5: Whose the current president of the United States in 2024?\nAnswer: ")
    if answer5 == "Joe Biden":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe answer is Joe Biden")
    
    answer6 = input("\nQuestion 6: What company owns Xbox?\nAnswer: ")
    if answer6 == "Microsoft":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is Microsoft")
    
    answer7 = input("\nQuestion 7: Which of the following is a Playstation exclusive game?\n" +
                    "A. Fallout\nB. Titanfall\nC. God of War\nD. Minecraft\nAnswer: ")
    if answer7 == "C":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer was C. God of War")
    
    answer8 = input("\nQuestion 8: What does CPU stand for?\nAnswer: ")
    if answer8 == "Central Processing Unit":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is Central Processing Unit")
    
    answer9 = input("\nQuestion 9: What superhero is referred to as the 'Man of Steel'?\nAnswer: ")
    if answer9 == "Superman":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is Superman")
    
    answer10 = input("\nQuestion 10: What does Programming Language is used in this program?\nAnswer: ")
    if answer10 == "Python":
        print("Correct!")
        points+= 1
    else:
        print("Incorrect!\nThe correct answer is Python")

    return points

def checkScore(points):
    if points == 10:
        print(f'You got a perfect score!')
    elif points <= 9 and points >= 6:
        print(f'You did good!')
    elif points == 5:
        print(f'You did fine.')
    elif points <= 4 and points > 0:
        print(f"You didn't do well")
    elif points == 0:
        print(f'You got no points.')


def main():
    name = message()
    game = questions()

    print(f'\nYour score is {game}/10')
    checkScore(game)
    print(f'\nThanks for playing {name}')

main()


