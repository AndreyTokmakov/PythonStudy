
if __name__ == '__main__':
    age = 28
    name = 'Jonh'
    month_salary = 5000

    # using format() function:
    print('Name: {}, age: {}, annual salary: {}'.format(name, age, 12 * month_salary))

    # using formatted string
    print(f'Name: {name}, age: {age}, annual salary: {12 * month_salary}')

    # using formatted string: same as above
    str_to_print = f'Name: {name}, age: {age}, annual salary: {12 * month_salary}'
    print(str_to_print)
