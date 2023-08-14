TEST_FILE_PATH: str = '../data/TestFile.txt'


def open_close_file():
    file = open(TEST_FILE_PATH, 'r')

    print(f'File name: {file.name}')
    print(f'Closed   : {file.closed}')

    file.close()


def open_close_file_GOOD():
    with open(TEST_FILE_PATH, 'r') as file:
        print(f'File name: {file.name}')
        print(f'Closed   : {file.closed}')

    print(f'\nFile name: {file.name}')
    print(f'Closed   : {file.closed}')  # Will be closed


def read_file_line():
    with open(TEST_FILE_PATH, 'r') as file:
        line = file.readline()
        print(line)


def read_file_all_lines():
    with open(TEST_FILE_PATH, 'r') as file:
        for line in file:
            print(line, end='')


def __read_file_lines_as_list():
    return [line.rstrip('\n') for line in open(TEST_FILE_PATH)]


def read_file_lines_as_list():
    lines = __read_file_lines_as_list()
    print(lines)


if __name__ == '__main__':
    # open_close_file()
    # open_close_file_GOOD()

    # read_file_line()
    # read_file_all_lines()
    read_file_lines_as_list()
