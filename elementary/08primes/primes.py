# http://adriann.github.io/programming_problems.html
# Write a program that prints all prime numbers.

class Prime():
    prime_list = []

def is_it_prime(number):
    if number < 4:
        return True
    else:
        for i in range(1, len(prime.prime_list)):
            if number % prime.prime_list[i] == 0:
                return False
    return True

prime = Prime()

for i in range(1, 50000):
    if is_it_prime(i) is True:
        prime.prime_list.append(i)

print(prime.prime_list)
print('This list has {} items.'.format(len(prime.prime_list)))
