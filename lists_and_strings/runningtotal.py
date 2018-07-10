# https://adriann.github.io/programming_problems.html
# Write a function that computes the running total of a list.

from odd_position import gen_list, get_number_of_items

def running_total(generate_ints, num_items, list_ints):
    total = 0
    for i in range(num_items):
        next_item = next(generate_ints)
        list_ints.append(next_item)
        total = total + next_item
        print('Running total is {}'.format(total))
    return total

def main():
    list_ints = []
    num_items = get_number_of_items()
    generate_ints = gen_list(num_items)
    running_tot = running_total(generate_ints, num_items, list_ints)
    print(list_ints)
    
if __name__ == '__main__':
    main()


