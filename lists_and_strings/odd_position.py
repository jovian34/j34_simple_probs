# https://adriann.github.io/programming_problems.html
# Write a function that returns the elements on odd positions in a list.

import random

def gen_list(num_items):
    for i in range(num_items):
        yield random.randint(1, 1000)

def get_odd_elements(generate_ints, num_items, list_ints):
    odds = []
    for i in range(num_items):
        next_item = next(generate_ints)
        list_ints.append(next_item)
        if i % 2 != 0:
            odds.append(next_item)
    return odds

def get_number_of_items():
    print('How many items are in this list?')
    try:
        number_of_items = abs(int(input()))
    except ValueError:
        return get_number_of_items()
    return number_of_items

def main():
    list_ints = []
    num_items = get_number_of_items()
    generate_ints = gen_list(num_items)
    odds = get_odd_elements(generate_ints, num_items, list_ints)
    print('List and the list items at odd offset postions')
    print(list_ints)
    print(odds)
    
if __name__ == '__main__':
    main()
