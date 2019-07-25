import random

print('AGE GAME')

age = random.randint(0, 100)

guess = -1

while guess != age:
    guess_text = input('Guess my age: ')
    guess = int(guess_text)

    if guess > age:
        print('I am younger than {}'.format(guess))
    elif guess < age:
        print('I am older than {}'.format(guess))

print('Correct, I am {}'.format(guess))
