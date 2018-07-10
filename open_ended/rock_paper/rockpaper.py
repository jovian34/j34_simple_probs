import players

def showdown(human_choice, computer_guess, h_obj, c_obj):
    if (human_choice, computer_guess) == (1, 3):
        print('Rock crushes scissors. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
    elif (human_choice, computer_guess) == (1, 2):
        print('Paper smothers rock. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
    elif (human_choice, computer_guess) == (2, 1):
        print('Paper smothers rock. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
    elif (human_choice, computer_guess) == (2, 3):
        print('Scissors cut paper. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
    elif (human_choice, computer_guess) == (3, 2):
        print('Scissors cut paper. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
    elif (human_choice, computer_guess) == (3, 1):
        print('Rock crushes scissors. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
    elif (human_choice, computer_guess) == (1, 1):
        print('Were all getting our Rocks on today!')
        print('------------------------------------')
    elif (human_choice, computer_guess) == (2, 2):
        print('Paper is on sale at Office Depot!!!!')
        print('------------------------------------')
    elif (human_choice, computer_guess) == (3, 3):
        print('Scissors! Dead Again is a great movie!')
        print('--------------------------------------')
    else:
        print('Hmmm... something is wrong with the code.')
     

def main():
    human = players.Human()
    computer = players.Computer()
    while human.score < 10 and computer.score < 10:
        print('Human: {} ... '
              'Computer: {}'.format(human.score, computer.score))
        print('====================================================')
        showdown(human.user_output(),computer.get_random(), human, computer)
    if human.score > computer.score:
        print('Human wins by score '
              'of {} to {}'.format(human.score, computer.score))
    else:
        print('Computer wins by score '
              'of {} to {}'.format(computer.score, human.score))

if __name__ == '__main__':
    main()
    
        


