from curr_constants import CURR_NAMES, CURR_VALUES
from change_to_return import get_inputs, calculate_change

coins = CURR_VALUES
price, payment = get_inputs()
value = calculate_change(price, payment)

coin_floor = [ value // coin for coin in coins ]

poss_gen = ([i,j,k,l,m,n,o,p,q,r] for i in range(coin_floor[0] + 1)
    for j in range(coin_floor[1] + 1)
    for k in range(coin_floor[2] + 1)
    for l in range(coin_floor[3] + 1)
    for m in range(coin_floor[4] + 1)
    for n in range(coin_floor[5] + 1)
    for o in range(coin_floor[6] + 1)
    for p in range(coin_floor[7] + 1)
    for q in range(coin_floor[8] + 1)
    for r in range(coin_floor[9] + 1))

print('generator is built')

def generate_results():
    for poss in poss_gen:
        total = 0
        for i in range(10):
            total += coins[i] * poss[i]
        if total == value:
            yield poss

print('results generator is created')

results = generate_results()

counter = 0

with open('results.txt', mode='w') as f:
    for result in results:
        for i in range(10):
            if result[i] > 0:
                f.write('{0} {1}, '.format(result[i], CURR_NAMES[i]))
        f.write('\n')
        counter += 1

print("There are {0} possibile ways to give ${1} in change.".format(counter, value/100 ))
