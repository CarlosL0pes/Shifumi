import random


def play():
    user = input(
        "Quelle est votre choix ? 'rock' pour pierre , 'paper' pour papier, 'scissors'  pour ciseaux\n ")
    computer = random.choice(['rock', 'paper', 'scissors'])
    print("L'ordinateur a choisi: ", computer)

    if user == computer:
        return 'Egalité!'

# r > s, s > p, p > r
    if is_win(user, computer):
        return 'Vous avez Gagné!'

    return 'Vous avez Perdu!'


def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r

    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
            or (player == 'paper' and opponent == 'rock'):
        return True


print(play())
