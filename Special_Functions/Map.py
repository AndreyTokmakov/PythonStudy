

def square(val):
    return val ** 2


if __name__ == '__main__':

    values = list(range(10))
    print(f"Values: {values}")

    print(list(map(square, values)))
    print(list(map(lambda x: x ** 2, values)))
