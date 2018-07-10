# http://adriann.github.io/programming_problems.html
# Write a program that asks the user for his name and greets him with his name.

def ask_user_for_name():
    print('What is your name?')
    return input()

def greet_user(name):
    print('Hello, {}'.format(name))

if __name__ == '__main__':
    user_name = ask_user_for_name()
    greet_user(user_name)
