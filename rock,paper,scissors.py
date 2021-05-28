import random

def play():
    randomchoice = random.randint(0,2)
    print(randomchoice)
    user_choice = input("What do you wanna use (0 = rock, 1 = paper, 2 = scissors): ")
    user_choice = int(user_choice)
    if user_choice == 0:
        choice = 0
    elif user_choice == 1:
        choice = 1
    elif user_choice == 2:
        choice = 2
    else:
        print("invalid input. try again")
        play()

    if randomchoice == choice:
        print("Tie")
    elif(randomchoice == 1 and choice == 0 or randomchoice == 0 and choice == 2 or randomchoice == 2 and choice == 1):
        print("Computer won")
    else:
        print("User won")

play()