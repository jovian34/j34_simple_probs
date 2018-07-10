# https://adriann.github.io/programming_problems.html
# Write three functions that compute the sum of the numbers in a list
# using a for-loop, a while-loop and recursion.

from occurs_in_list import make_random_list, get_elements

def sum_for(list_to_sum):
    sum_list = 0
    for i in range(0, len(list_to_sum)):
        sum_list = sum_list + list_to_sum[i]
    return sum_list

def sum_while(list_to_sum):
    sum_list = 0
    i = 0
    while i < len(list_to_sum):
        sum_list = sum_list + list_to_sum[i]
        i += 1
    return sum_list

def sum_recurse(recurse_list, total):
    if len(recurse_list) > 0:
        total = total + recurse_list[0]
        recurse_list.remove(recurse_list[0])
        return sum_recurse(recurse_list, total)
    else:
        return total

def main():
    length, high_num = get_elements()
    list_to_sum = make_random_list(length, high_num)
    print(list_to_sum)
    sum_for_result = sum_for(list_to_sum)
    sum_while_result = sum_while(list_to_sum)
    recurse_list = list_to_sum
    sum_recurse_result = sum_recurse(recurse_list, 0)
    print('Sum by for-loop: {}. '
          'Sum by while-loop: {}. '
          'Sum by recursion: {}.'.format(sum_for_result,
                                        sum_while_result,
                                        sum_recurse_result))

if __name__ == '__main__':
    main()
