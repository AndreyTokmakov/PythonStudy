def create_set():
    set_one = set()

    print(type(set_one), len(set_one))

    set_two = {1}
    not_the_set = {}

    print(type(set_two), len(set_two))
    print(type(not_the_set), len(not_the_set))

    set_three = {1, 2, 3, 4, 5}
    print(set_three, f'size of set = {len(set_three)}')


def add_elements_to_the_set():
    my_set = {1, 2, 3, 4}

    my_set.add(5)
    print(my_set)

    #  add multiple elements to the set
    my_set.update([6, 7, 8])
    print(my_set)


def remove_first_elements():
    my_set = {1, 2, 3, 4}

    my_set.pop()
    print(my_set)


def remove_specific_element():
    my_set = {1, 2, 3, 4}

    my_set.remove(2)
    print(my_set)


def check_if_element_exist():
    my_set = {1, 2, 3, 4}

    is_3_exist = (3 in my_set)
    print(is_3_exist)

    is_5_exist = (5 in my_set)
    print(is_5_exist)


def find_unique_elements():
    some_test_list = [1, 2, 3, 2, 4, 1, 5]
    print(some_test_list)

    my_set = set(some_test_list)
    print(my_set)


if __name__ == '__main__':
    # create_set()

    # add_elements_to_the_set()

    # remove_first_elements()
    # remove_specific_element()

    # check_if_element_exist()

    find_unique_elements()