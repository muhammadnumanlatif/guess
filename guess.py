import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while  guess != random_number:
        guess = int(input(f'Guess the number b/w 1 and {x}'))
        if guess < random_number:
            print('The number is too low!')
        elif guess > random_number:
            print('The number is too high!')
    print(f'Wow! You are right: {random_number}')

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while  feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            high = guess + 1
    print(f'Wow! Computer is right: {guess}')