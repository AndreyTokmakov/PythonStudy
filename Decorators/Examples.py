def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def greet(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    greet("Jonh")
