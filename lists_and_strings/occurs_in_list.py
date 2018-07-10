# https://adriann.github.io/programming_problems.html
# Write a function that checks whether an element occurs in a list.

import random

def make_random_list(length, high_num):
    set_ints = set()
    while len(set_ints) < length:
        set_ints.add(random.randint(1, high_num))
    list_ints = list(set_ints)
    return list_ints        

def element_in_list(list_obj, element):
    for i in range(len(list_obj)):
        if element == list_obj[i]:
            return True
    return False

def get_elements():
    print('How many items in the list? ', end='')
    length = input()
    print('What is the highest possible value?')
    print('*Must be higher than size of list: ', end='')
    high_num = input()
    try:
        length = abs(int(length))
        high_num = abs(int(high_num))
    except ValueError:
        print('Value must be a whole number... try again.')
        return get_elements()
    if length >= high_num:
        print('*High value must be higher than size of list... try again.')
        return get_elements()
    return (length, high_num)

def make_a_guess():
    print('What value do you think is in the list? ', end='')
    element = input()
    try:
        element = abs(int(element))
    except ValueError:
        print('Guess must be a whole number... try again.')
        return make_a_guess()
    return element
    

def main():
    length, high_num = get_elements()
    list_ints = make_random_list(length, high_num)
    element = make_a_guess()
    if element_in_list(list_ints, element):
        print('CONGRATS! Your guess {} is '
              'in list {}.'.format(element, list_ints))
    else:
        print('Sorry. Your guess {} is '
              'NOT in list {}.'.format(element, list_ints))
    print('================================================')
    print('Play again? y or n? ', end='')
    y_or_n = input()
    if y_or_n[0] == 'y':
        main()
    elif y_or_n[0] == 'n':
        print('Have a nice day!')
    else:
        raise ValueError('lower case y or n required! END PROGRAM!')
        

if __name__ == '__main__':
    main()
