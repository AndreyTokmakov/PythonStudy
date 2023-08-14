TEST_FILE_PATH: str = '../data/TestFile2.txt'


def write_to_file():
    with open(TEST_FILE_PATH, 'w') as file:
        file.write("TEST1")


def append_to_file():
    with open(TEST_FILE_PATH, 'a') as file:
        file.write("two\n")


if __name__ == '__main__':
    # write_to_file()
    # append_to_file()

    value: str = 'ss'

    var: int = int(value) if value.isdigit() else 0
    print(var)
