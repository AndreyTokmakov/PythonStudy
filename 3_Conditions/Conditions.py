if __name__ == '__main__':
    one = 1
    two = 2
    three = 3
    one_1 = 1

    print('------------------------------------ greater ---------------------------------------------\n')

    if two > one:
        print(f'{two} greater than {one}')

    if two > three:
        print(f'{two} greater than {three}')
    else:
        print(f'Else: {two} NOT greater than {three}')

    print('\n------------------------------------ less ---------------------------------------------\n')

    if one < two:
        print(f'{one} less than {two}')

    if two < one:
        print(f'{one} less than {two}')
    else:
        print(f'Else: {two} NOT less than {one}')

    print('\n------------------------------------ equal  ---------------------------------------------\n')

    if one == one_1:
        print(f'{one} is equal {one_1}')

    if one == two:
        print(f'{one} is equal {two}')
    else:
        print(f'Else: {one} NOT equal {two}')

    print('\n------------------------------------ greater or equal ---------------------------------------------\n')

    if two >= one:
        print(f'{two} greater or equal than {one}')

    if two >= two:
        print(f'{two} greater or equal than {two}')

    print('\n------------------------------------ less or equal ---------------------------------------------\n')

    if one <= two:
        print(f'{one} less or equal than {two}')

    if two <= two:
        print(f'{two} less or equal than {two}')

    # 10 < x 20

    # != None

    # Multiple | age_0 >= 21 and age_1 >= 21

    # else if

    '''
    requested_topping = 'mushrooms'
    if requested_topping != 'anchovies':
        print("Hold the anchovies!")
    '''

    '''
    print(one == one_1)
    print(one == two)
    '''
