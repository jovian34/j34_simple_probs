# http://adriann.github.io/programming_problems.html
# Write a program that asks the user for a number n and prints
# the sum of the numbers 1 to n

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

def main():
    user_number = get_number_from_user()
    try:
        user_number = int(user_number)
    except:
        print('This program only works on integer values.')
        print('Please try again')
        return main()
    sum_num = sum_range(user_number)
    print('The sum of the numbers from 1 to {} is {}.'.format(user_number,
                                                              sum_num))


if __name__ == '__main__':
    main()
