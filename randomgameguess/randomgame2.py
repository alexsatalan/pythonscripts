from random import randint
import sys

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print(f'hey bozo, I said between 0 and 10!')
        return False

if __name__ == '__main__':
    answer = randint(0, 10)
    while True:
        try:
            guess = int(input(f'guess a number between 0 and 10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
