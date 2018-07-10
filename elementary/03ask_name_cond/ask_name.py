# http://adriann.github.io/programming_problems.html
# Write a program that asks the user for his name and greets him with his name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def ask_user_for_name():
    print('What is your name?')
    return input()

def greet_user(name):
    print('Hello, {}'.format(name))

def check_for_alice_or_bob(name):
    lower_name = name.lower()
    if lower_name == 'alice' or lower_name == 'bob':
        greet_user(name)

if __name__ == '__main__':
    user_name = ask_user_for_name()
    check_for_alice_or_bob(user_name)
