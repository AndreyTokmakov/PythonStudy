
def print_user_info(name, age):
    print(f'User: {name}, Age: {age}')


if __name__ == '__main__':
    print_user_info('Jonh', 38)
    print_user_info(38, 'Jonh')

    print()

    print_user_info(name='Jonh', age=38)
    print_user_info(age=38, name='Jonh')

