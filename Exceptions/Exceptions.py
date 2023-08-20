def divide(a, b):
    print(a / b)


def divide_safe(a, b):
    try:
        print(a / b)
    except:
        print(0)


def divide_safe_2(a, b):
    try:
        print(a / b)
    except Exception as exc:
        print(f'Error: {exc}')
        print(0)


def print_list_element(list, idx):
    try:
        print(f'{idx} element is {list[idx]}')
    except Exception as exc:
        print(f'Error: {exc}')
        print(0)


if __name__ == "__main__":
    # divide(10, 0)

    # divide_safe(10, 0)
    # divide_safe_2(10, 0)

    print_list_element([0, 1, 2, 3, 4, 5], 3)
    print_list_element([0, 1, 2, 3, 4, 5], 13)
