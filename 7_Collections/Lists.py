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


def add_to_list():
    list = []

    list.append("val1")
    list.append(2)
    list.append("val3")
    list.append(4)
    list.append("val5")

    print(list)


def clear_list():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    numbers.clear()
    print(numbers)


def pop_values():
    numbers = [1, 2, 3, 4, 5]
    print(numbers, "\n")

    for _ in range(4):
        numbers.pop()
        print(numbers)


if __name__ == '__main__':
    # create_list()
    # sort_list()
    # add_to_list()
    # clear_list()
    pop_values()

    # append
    # pop
    

