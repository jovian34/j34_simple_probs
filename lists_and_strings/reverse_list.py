# https://adriann.github.io/programming_problems.html
# Write function that reverses a list, preferably in place.

def reverse_list(list):
    rev_list = []
    for i in range(len(list)):
        rev_list.append(list[-i -1])
    return rev_list

def make_list(length):
    master_list = []
    for i in range(length):
        master_list.append(i)
    return master_list

def main():
    master_list = make_list(10)
    print(master_list)
    print(reverse_list(master_list))

if __name__ == '__main__':
    main()
