def create():
    test_dict = {'one': 1, 'two': 2, 'three': 3}
    print(test_dict)


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


if __name__ == '__main__':
    # create()
    # get_or_access_element()

    # access_element_missing()
    # get_element_missing()

    # add_elements()

    # modify_elements()

    # loop_enumerate_dict()
    loop_enumerate_keys()

    # delete
    # enumerate
    # modify
