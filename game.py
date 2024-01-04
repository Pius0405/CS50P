import random
import sys

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            # positive integer is >0 and is int
            #check if level is positive integer
            if level > 0 and isinstance(level, int):
                break
        except ValueError:
            pass
    return level

def get_guess():
    while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0 and isinstance(guess, int):
                break
        except ValueError:
            pass
    return guess

def main():
    level = get_level()
    random_num = random.randint(1,level)
    guess = get_guess()
    while True:
        if guess == random_num:
            sys.exit('Just right!')
        elif guess > random_num:
            print('Too large!')
            guess = get_guess()
        else:
            print('Too small!')
            guess = get_guess()

main()
