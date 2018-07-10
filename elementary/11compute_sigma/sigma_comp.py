# https://adriann.github.io/programming_problems.html
# Write a program that computes
#   4⋅∑k=1106(-1)k+12k-1=4⋅(1-1/3+1/5-1/7+1/9-1/11…).


def calc_sigma():
    result = 0.0
    for k in range(1, 1000000):
        numer = -1 ** (k + 1)
        numer = float(numer)
        denom = 2 * k - 1
        denom = float(denom)
        result += numer/denom
    return result

def main():
    print(4.0 * calc_sigma())

if __name__ == '__main__':
    main()
