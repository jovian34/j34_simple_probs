import random


def base_strategy(player_nums, computer_nums):
    if len(computer_nums) < 3:
        return random.randrange(1, 4)
    else:
        base_guess = computer_nums[-2]
        if base_guess == 1:
            return 2
        if base_guess == 2:
            return 3
        else:
            return 1

    '''
    return random.randrange(1, 4)
    guess = input('What is your guess? ')
    guess = int(guess)
    if guess < 1:
        print('Your gues must be at least 1!')
        return base_strategy
    return guess
    '''


def computer_strategy(scores, player_answers, computer_answers,
        total_iterations, current_iteration):
    # ADD YOUR SOLUTION HERE
    if len(player_answers) == 0:
        return random.randrange(1, 4)
    random_factor = random.randrange(1, 4)
    if random_factor == 2:
        return 2
    if player_answers[-1] > 1:
        return 1
    else:
        return 3


def compute_score(player_answer, computer_answer, scores):
    if player_answer + 1 == computer_answer:
        scores['computer'] += 2
    elif computer_answer + 1 == player_answer:
        scores['player'] += 2
    elif player_answer < computer_answer:
        scores['player'] += 1
    elif player_answer > computer_answer:
        scores['computer'] += 1
    return scores


def calculate_winner(scores, outcomes):
    if scores['player'] > scores['computer']:
        outcomes['player'] += 1
    elif scores['computer'] > scores['player']:
        outcomes['computer'] += 1
    else:
        outcomes['ties'] += 1
    return outcomes


# run!

if __name__ == '__main__':
    iterations = 1000
    scores = {'player': 0, 'computer': 0}
    outcomes = {'player': 0, 'computer': 0, 'ties': 0}
    player_nums = []
    computer_nums = []
    for x in range(0, iterations):
        while scores['player'] < 5 and scores['computer'] < 5:
            player_answer = base_strategy(player_nums, computer_nums)
            computer_answer = computer_strategy(
                scores, player_nums, computer_nums, iterations, x)
            #print('Computer Guess: {}'.format(computer_answer))
            player_nums.append(player_answer)
            computer_nums.append(computer_answer)
            compute_score(player_answer, computer_answer, scores)
            #print(scores)
        calculate_winner(scores, outcomes)
        scores = {'player': 0, 'computer': 0}
        player_nums = []
        computer_nums = []
    print('Results - Player {0}, Computer {1}, Tie {2}'.format(
        outcomes['player'], outcomes['computer'], outcomes['ties']))
