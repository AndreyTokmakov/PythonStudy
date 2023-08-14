def hello():
    """ Display a simple hello message """
    print('Hello from function')


def hello_input():
    name = input('Enter your name:')
    print(f'Hello {name}')


# Python Functions is a block of statements that return the specific task
# The idea is to put some commonly or repeatedly done tasks together and make a function so that
# instead of writing the same code again and again for different inputs,
# we can do the function calls to reuse code contained in it over and over again.

'''  Function syntax:

    def SOME_FUNCTION_NAME ():
        ---- function body ----

'''

if __name__ == '__main__':
    hello()

    # hello_input()
