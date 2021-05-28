import random
winner = ''
computer_pt = 0
spieler_pt = 0
def spielen():
    random_choice = random.randint(0,2)
    print(random_choice)
    if random_choice == 0:
        computer_choice = 'rock'
    elif random_choice == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'
    user_choice = input('rock, paper or scissors? ')
    if computer_choice == user_choice:
        winner = 'Tie'
    elif  ( computer_choice == 'paper' and user_choice == 'rock' or computer_choice == 'rock' and user_choice == 'scissors' or computer_choice == 'scissors' and user_choice == 'paper') :
        winner = 'Computer'

    else:
        winner = 'User'
    if winner == 'Tie':
        print('We both chose', computer_choice + ', play again.')
    else:
        print(winner, 'won. The computer chose', computer_choice + '.')
    return winner
while computer_pt < 3 and spieler_pt < 3:
    print (str(computer_pt) +"< 3  or  "+str(spieler_pt) + " < 3")
    thewinner = spielen()
    if thewinner == 'computer':
        computer_pt += 1
    elif thewinner == 'User':
        spieler_pt += 1