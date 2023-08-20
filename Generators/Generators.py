def generator_example():
    generator_values = (x for x in [1, 2, 3, 4, 5, 6])

    counter = 0
    for val in generator_values:
        print(val)
        counter += 1
        if counter == 3:
            break

    print()

    for val in generator_values:
        print(val)


def list_example():
    # list = [x for x in [1, 2, 3, 4, 5, 6]]
    list = [1, 2, 3, 4, 5, 6]

    counter = 0
    for val in list:
        print(val)
        counter += 1
        if counter == 3:
            break

    print()

    for val in list:
        print(val)


if __name__ == '__main__':
    list_example()
    # generator_example()
