# http://adriann.github.io/programming_problems.html
# Write a program that asks the user for a number n and prints
# the sum of the numbers 1 to n
# Modify the previous program such that only multiples of three or
# five are considered
# in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

def get_number_from_user():
    print('Enter a number: ', end='')
    return input()

def sum_range(number):
    sum_total = 0
    for i in range(1, number + 1):
        print(i, end='')
        sum_total = sum_total + i
        print('...{}'.format(sum_total))
    return sum_total

def sum_range_of_multiples(number):
    sum_total = 0
    for i in range(1, number + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_total = sum_total + i
            print('{} ... {}'.format(i, sum_total))
    return sum_total

def main():
    user_number = get_number_from_user()
    try:
        user_number = int(user_number)
    except:
        print('This program only works on integer values.')
        print('Please try again')
        return main()
    sum_num = sum_range_of_multiples(user_number)
    print('The sum of the multiple of 3 and 5 from 1 to '
          '{} is {}.'.format(user_number, sum_num))

if __name__ == '__main__':
    main()
