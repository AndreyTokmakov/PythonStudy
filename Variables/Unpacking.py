def get_values():
    return 10, 20, 30, 40


def get_strings():
    return "I", "II", "III", "IV"


def get_list():
    return ["one", "two", "three", "four"]


def get_big_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if __name__ == "__main__":
    a, b, c = 1, 2, 3
    print(a, b, c)

    a, b, c, d = get_values()
    print(a, b, c, d)

    a, b, c, d = get_strings()
    print(a, b, c, d)

    a, b, c, d = get_list()
    print(a, b, c, d)

    first, second, third, *other = get_big_list()
    print(first, second, third, other)
