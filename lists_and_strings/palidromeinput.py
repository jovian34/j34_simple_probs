# https://adriann.github.io/programming_problems.html
# Write a function that tests whether a string is a palindrome.

from palindrome import Palindrome

def get_word_from_user():
    print('Type word you want to check for Palindrome: ', end='')
    word = input()
    word = word.lower()
    return word

def main():
    word = get_word_from_user()
    palindrome = Palindrome()
    if palindrome.check_palindrome(word):
        print('{} is a palindrome!'.format(word))
    else:
        print('{} is not a palindrome!'.format(word))
    
if __name__ == '__main__':
    main()
