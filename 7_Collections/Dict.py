def create_empty():
    test_dict = {}
    print(test_dict)
    print(f'length: {len(test_dict)}')

    print()

    test_dict1 = dict()
    print(test_dict1)
    print(f'length: {len(test_dict1)}')


def create():
    test_dict = {'one': 1, 'two': 2, 'three': 3}
    print(test_dict)
    print(f'length: {len(test_dict)}')


def get_or_access_element():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    print(test_dict['one'])  # Print: 1
    print(test_dict.get('two'))  # Print: 2


def access_element_missing():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    print(test_dict['four'])  # Here we will get KeyError: 'four' since there is no element with key 'four'


def get_element_missing():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    # get(key) --> returns the required element or None if missing

    print(test_dict.get('four'))  # Print: None

    # get(key, default_value) --> returns the required element or 'default_value' if missing

    print(test_dict.get('four', 100500))  # Print: 100500


def add_elements():
    test_dict = {}

    test_dict['one'] = 1
    test_dict['two'] = 2

    print(test_dict)


def modify_elements():
    test_dict = {}

    test_dict['one'] = 1
    print(test_dict)

    test_dict['one'] = 2
    print(test_dict)


def loop_enumerate_dict():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    for key, value in test_dict.items():
        print(f'{key} = {value}')


def loop_enumerate_keys():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    for key in test_dict.keys():
        print(f'{key}')

    # + get value using key in loop
    for key in test_dict.keys():
        print(f'{key} = {test_dict.get(key)}')


def loop_enumerate_values():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    for val in test_dict.values():
        print(val)


def Pop():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    val_poped = test_dict.pop('two')

    print(f'val_poped: {val_poped}')
    print(f'test_dict: {test_dict}')


def check_if_key_exist():
    test_dict = {'one': 1, 'two': 2, 'three': 3}

    key = 'one'
    if key in test_dict:
        print(f'{key} exits')
    else:
        print(f'{key} is missing')

    print()

    if test_dict.get(key):
        print(f'{key} exits')
    else:
        print(f'{key} is missing')

    print()

    key = 'six'
    if key in test_dict:
        print(f'{key} exits')
    else:
        print(f'{key} is missing')


if __name__ == '__main__':
    create_empty()
    # create()

    # get_or_access_element()

    # access_element_missing()
    # get_element_missing()

    # add_elements()

    # modify_elements()

    # loop_enumerate_dict()
    # loop_enumerate_keys()
    # loop_enumerate_values()

    # Pop()

    # check_if_key_exist()
