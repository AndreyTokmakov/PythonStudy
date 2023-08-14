
def create_tuple():
    tup = tuple()
    print(tup)

    tup2 = ('a', 'b',)
    print(tup2)

    tup3 = tuple('ABC')
    print(type(tup3))

    tup4 = (1, 2, 3, 4, 5, 6)
    print(tup4)


def print_tuple_values():
    test_tuple = ('Value1', 'Value2', 'Value3', 'Value4', 'Value5')
    for val in test_tuple:
        print(val)


def get_tuple_elements():
    test_tuple = ('one', 'two', 'three')
    print(test_tuple[0])
    print(test_tuple[1])
    print(test_tuple[2])


def compare():
    tup1 = (202, 'OK')
    tup2 = (202, 'OK')
    tup3 = (202, 'Not sure')

    print(tup1 == tup2)
    print(tup1 == tup3)


if __name__ == '__main__':
    # create_tuple()
    # print_tuple_values()
    # compare()
    get_tuple_elements()
