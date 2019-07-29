import random


def main():
    print_header()
    game_loop()


def print_header():
    print('RICK AND MORTY BATTLE!')


def game_loop():

    contestants = ['Rick 1', 'Rick 2', 'Morty 1', 'Morty 2']
    print('The contestants are {}'.format(contestants))

    print('The battle begins...')
    while len(contestants) > 1:
        defeated = random.choice(contestants)
        print('{} is defeated'.format(defeated))
        contestants.remove(defeated)

    winner = contestants[0]

    print('{} wins the battle'.format(winner))


if __name__ == '__main__':
    main()
