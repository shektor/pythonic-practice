import random

print('AGE GAME')

age = random.randint(0, 100)

guess = -1

while guess != age:
    guess_text = input('Can you guess my age? ')
    guess = int(guess_text)

    if guess > age:
        print('I am younger than ' + guess_text)
    elif guess < age:
        print('I am older than ' + guess_text)

print('Yes, I am ' + guess_text)
