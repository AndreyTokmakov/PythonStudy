def simple_test():
    ints = [1, 2, 3, 4, 5]

    # create / get the Iterator to beginning of the list 'ints'
    it = iter(ints)

    print(next(it))
    print(next(it))
    print(next(it))


def range_Loop_test():
    for i in iter(range(5)):
        print(i)


def our_of_range():
    ints = [1, 2, 3]

    # create / get the Iterator to beginning of the list 'ints'
    it = iter(ints)

    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))  # here we're trying to get the 4-th element of list
                     # StopIteration Exception will be raised


if __name__ == "__main__":
    # simple_test()
    # range_Loop_test()
    our_of_range()
