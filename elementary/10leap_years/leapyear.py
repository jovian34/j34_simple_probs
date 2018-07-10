# https://adriann.github.io/programming_problems.html
# Write a program that prints the next 20 leap years.

from datetime import date

def next_x_leap_years(x):
    day = date.today()
    leap_years = []
    while len(leap_years) < x:
        try:
            day = day.replace(year = day.year + 1, month = 2, day = 29)
            leap_years.append(day.year)
        except ValueError:
            day = day.replace(year = day.year + 1, month = 3, day = 1)
    return leap_years

def get_num_of_leap_years():
    print('How many leap years do you want to generate? ', end='')
    num = input()
    try:
        num = int(num)
    except:
        print('Invalid entry: please enter a number.')
        return get_num_of_leap_years()
    return num

def main():
    number = get_num_of_leap_years()
    leap_years = next_x_leap_years(number)
    print('The next {} leap years are:'.format(number))
    for i in range(len(leap_years)):
        if i < 9:
            print(' {}) {}'.format(i + 1, leap_years[i]))
        else:
            print('{}) {}'.format(i + 1, leap_years[i]))

if __name__ == '__main__':
    main()
