class User(object):
    # Class without any params and methods
    pass


if __name__ == '__main__':

    text: str = 'hello world'
    integer_value: int = 100
    float_value: float = 100.01
    some_list = [1, 2, 3]
    some_dict = {1: "", 2: ""}
    some_tupple = (1, 2, 3)
    user = User()

    print(f'"text" variable type is {type(text)}')
    print(f'"integer_value" variable type is {type(integer_value)}')
    print(f'"float_value" variable type is {type(float_value)}')
    print(f'"some_list" variable type is {type(some_list)}')
    print(f'"some_dict" variable type is {type(some_dict)}')
    print(f'"some_tupple" variable type is {type(some_tupple)}')
    print(f'"user" variable type is {type(user)}')
