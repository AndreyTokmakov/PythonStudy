
def print_list_element(list, idx):
    try:
        print(f'{idx} element is {list[idx]}')
    except Exception as exc:
        print(f'Error: {exc}')
    finally:
        print('This line will be called anyway\n')


if __name__ == "__main__":
    print_list_element([0, 1, 2, 3, 4, 5], 3)
    print_list_element([0, 1, 2, 3, 4, 5], 13)
