
def devidable_3(val):
    return 0 == val % 3

if __name__ == '__main__':

    values = list(range(10))
    print(f"Values: {values}")

    print(list(filter(devidable_3, values)))
    print(list(filter(lambda x: x % 3 == 0, values)))
