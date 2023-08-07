from typing import List


def create_list():
    ints = [0, 1, 2, 3, 4, 5]
    print(ints)

    numbers = [x for x in range(6)]
    print(numbers)

    str_list = ['zero', 'one', 'two', 'three', 'four', 'five']
    print(str_list)


def sort_list():
    numbers = [1, 5, 2, 3, 4]
    print(numbers)

    numbers.sort()
    print(numbers)

    numbers.sort(reverse=True)
    print(numbers)


if __name__ == '__main__':
    # create_list()
    sort_list()

    # append
    # pop
    

