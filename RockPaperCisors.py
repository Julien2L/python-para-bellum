import random

def play():
    user = input("Quel est votre choix ? 'r' pierre, 'p' for papier, 'c' ciseaux : \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Match Nul'

    if is_win(user, computer):
        return 'Vous avez gagnez !'

    return 'Vous avez perdu !'    

def is_win(player, opponent):
    if (player == 'r' and opponent == 'c') or (player == 'c' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())