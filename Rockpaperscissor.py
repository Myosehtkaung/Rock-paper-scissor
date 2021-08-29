import random

def game():
    user = input("Type 'r' for Rock, 'p' for Paper, 's' for Scissor: ")
    elements = ['r', 'p', 's']
    com = random.choice(elements)
    print(f"Computer types {com}.")

    while user == com:
        user = input("Type 'r' for Rock, 'p' for Paper, 's' for Scissor: ")
        com = random.choice(elements)
        print(f"Computer types {com}.")

    if win(user, com):
        return 'You Win'

    if win(com, user):
        return 'You lose'

def win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or \
            (player1 == 'p' and player2 == 'r'):
        return True

print(game())