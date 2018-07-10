import random

class Player(object):

    def __init__(self):
        self.score = 0

    def add_to_score(self):
        self.score += 1
        
class Human(Player):
    
    def _get_user_input(self):
        options = ['r', 'p', 's']
        print('choose (r)ock, (p)aper, or (s)cissors: ', end='')
        choice = input()
        if choice[0] in options:
            return choice[0]
        else:
            print('Invalid choice... please try again. *must be lowercase*')
            return _get_user_input()

    def _process_choice(self, choice):
        if choice[0] == 'r':
            print('You chose rock!')
            return 1
        if choice[0] == 'p':
            print('You chose paper!')
            return 2
        if choice[0] == 's':
            print('You chose scissors!')
            return 3

    def user_output(self):
        choice = self._get_user_input()
        return self._process_choice(choice)


class Computer(Player):

    def get_random(self):
        return random.randint(1, 3)

