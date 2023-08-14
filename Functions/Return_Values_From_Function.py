def get_hello_string():
    return "Hello"


def get_world_string():
    return "world"


def get_number():
    return 123


def get_banner():
    return get_hello_string() + " " + get_world_string()


if __name__ == '__main__':

    hello = get_hello_string()
    world = get_world_string()
    print(f'{hello} {world}')

    some_number = get_number()
    print(some_number)

    banner = get_banner()
    print(banner)
