import random
from characters import Player, Alien

def main():
    print_header()
    game_loop()


def print_header():
    print('RICK AND MORTY BATTLE!')


def game_loop():

    contestants = [
        Player('Rick', 100),
        Player('Morty', 10),
        Player('Summer', 25),
        Player('Beth', 50),
        Player('Jerry', 3),
        Alien('Amish Cyborg', 40, 2)
    ]

    print('The contestants are {}'.format(contestants))

    print('The battle begins...')
    while len(contestants) > 1:
        p1 = random.choice(contestants)
        p2 = random.choice(contestants)

        print('{} attacks {}'.format(p1, p2))

        if p1.attack() > p2.defense():
            print('{} is defeated'.format(p2))
            contestants.remove(p2)
        else:
            print('{} blocks'.format(p2))

    winner = contestants[0]

    print('{} wins the battle'.format(winner))


if __name__ == '__main__':
    main()
