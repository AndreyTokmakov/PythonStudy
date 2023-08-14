if __name__ == '__main__':

    # 1. Create string
    first_name = "Jonh"  # OK to use  "
    second_name = 'Dow'  # and its OK to use '
    text = '''Some long text. We can use quotation marks: "qwerty" and 'qwerty' '''

    print(first_name, second_name)
    print(text)

    # Get the string length - using the builtin len() method:
    length = len(first_name)
    print(f'The length of the {first_name} is {length}')

    print()  # just empty line

    # Access characters of String
    for idx in range(len(first_name)):
        symbol = first_name[idx]
        print(f'first_name[{idx}] = {symbol}')

    print()  # just empty line

    # Printing First character
    print("First character of String is: ", first_name[0])

    # Printing Last character
    print("Last character of String is : ", first_name[-1])
    print("Last character of String is : ", first_name[len(first_name) - 1])

    print()  # just empty line

    # String Slicing : Substrings
    hello = 'Hello world!'
    print(hello[0:5])  # Hello - substring from 0 til 5 symbols of the string
    print(hello[:5])  # Hello - substring from 0 til 5 symbols of the string (same as above)

    print()  # just empty line

    print(hello.lower())  # To Lower case : 'Hello world!' --> 'hello world!'
    print(hello.upper())  # To Lower case : 'Hello world!' --> 'HELLO WORLD!'

    print()  # just empty line

    # using split() to split string into the list
    text = 'one two three four five'
    parts = text.split(sep=' ')
    print(parts)
    for part in parts:
        print(part, end=' ')

    print()  # just empty line

    # using split() to split string into the list
    text = 'val1,val2,val3,val4,val5'
    parts = text.split(sep=',')
    print(parts)
    for part in parts:
        print(part, end=' ')
