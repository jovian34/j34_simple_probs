# https://adriann.github.io/programming_problems.html
# Write a function that returns the largest element in a list.

import random

def gen_list(num_items):
    for i in range(num_items):
        yield random.randint(1, 1000)

def get_largest(generate_ints, num_items, list_ints):
    largest = 0
    for i in range(num_items):
        next_item = next(generate_ints)
        list_ints.append(next_item)
        if largest < next_item:
            largest = next_item
    return largest

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
    largest = get_largest(generate_ints, num_items, list_ints)
    print('The largest value in your list is {}.'.format(largest))
    print(list_ints)
    
if __name__ == '__main__':
    main()
