# http://adriann.github.io/programming_problems.html
# Write a program that asks the user for a number n and gives him the possibility to
# choose between computing the sum and computing the product of 1,…,n.

def get_number_from_user():
    print('Enter a number: ', end='')
    return input()

def sum_range(number):
    sum_total = 0
    for i in range(1, number + 1):
        print(i, end='')
        sum_total = sum_total + i
        print('...{}'.format(sum_total))
    print('The sum of the numbers from 1 to {} is {}.'.format(number,
                                                              sum_total))

def mult_range(number):
    sum_total = 1
    for i in range(1, number + 1):
        print(i, end='')
        sum_total = sum_total * i
        print('...{}'.format(sum_total))
    print('The product of the numbers from 1 to {} is {}.'.format(number,
                                                              sum_total))

def choose_function(number):
    print('Do you want to:')
    print('    1) Compute the sum of a range from 1 to {}'.format(number))
    print('    2) Compute the prouct instead')
    choice = input()
    return choice

def get_number():
    user_number = get_number_from_user()
    try:
        user_number = int(user_number)
    except:
        print('This program only works on integer values.')
        print('Please try again')
        print('==========================================')
        return get_number()
    return user_number

def process_choice(number):
    choice = choose_function(number)
    if  choice == '1':
        sum_range(number)
    elif choice == '2':
        mult_range(number)
    else:
        print('Choice is invalid.')
        print('Please choose again')
        print('===================')
        return process_choice(number)
    
def main():
    user_number = get_number()
    process_choice(user_number)

if __name__ == '__main__':
    main()
