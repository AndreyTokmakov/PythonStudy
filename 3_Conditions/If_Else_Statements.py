
if __name__ == '__main__':

    value = 12

    if value < 4:
        print(f'{value} greater than 4')
    elif value < 18:
        print(f'{value} greater than 4 but less than 18')
    else:
        print(f'{value} greater than 18')

    print()

    if value < 4:
        print(f'{value} greater than 4')
    elif value < 10:
        print(f'{value} greater than 4 but less than 10')
    elif value < 18:
        print(f'{value} greater than 10 but less than 18')
    else:
        print(f'{value} greater than 18')

    print()

    if value < 4:
        print(f'{value} greater than 4')
    elif 10 < value < 18:
        print(f'{value} in range between 10 and 18')
    else:
        print(f'{value} greater than 18')
