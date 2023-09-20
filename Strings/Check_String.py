

if __name__ == '__main__':
    number_string: str = '12345'
    non_number_string: str = '1a2b3c4d5e'
    char_string: str = 'qwerty'

    print(f'String "{number_string}" contains only digits:', number_string.isdigit())
    print(f'String "{non_number_string}" contains only digits:', non_number_string.isdigit())

    print()

    print(f'String "{number_string}" contains only non digits:', char_string.isalpha())
    print(f'String "{non_number_string}" contains only non digits:', non_number_string.isalpha())

