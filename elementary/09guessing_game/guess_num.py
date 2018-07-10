# https://adriann.github.io/programming_problems.html
# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether
# his number was too large or too small.
# At the end the number of tries needed should be printed.
# I counts only as one try if the user inputs the same number consecutively.

import random

def get_secret_number():
    rand = random.randint(1, 1000)
    return rand

def get_guess():
    print('Enter your guess of the secret number between 1 and 1000: ', end='')
    guess = input()
    try:
        guess = int(guess)
    except ValueError:
        print('Your guess must be an integer.')
        print('Please try again.')
        return get_guess()
    return guess

def process_guess(guess, secret_num, set_guesses):
    set_guesses.add(guess)
    if guess == secret_num:
        print('{} is the number. Congratulations! '
              'You got it in {} tries.'.format(secret_num, len(set_guesses)))
    elif guess > secret_num:
        print('Sorry! That guess is too high.')
        print('Guesses so far: ', end='')
        print(set_guesses)
        print('==============================')
        new_guess = get_guess()
        return process_guess(new_guess, secret_num, set_guesses)
    else:
        print('Sorry! Your guess is too low.')
        print('Guesses so far: ', end='')
        print(set_guesses)
        print('=============================')
        new_guess = get_guess()
        return process_guess(new_guess, secret_num, set_guesses)
    
def main():
    guesses = set()
    guess = get_guess()
    secret = get_secret_number()
    process_guess(guess, secret, guesses)

if __name__ == '__main__':
    main()
