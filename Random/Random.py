import random

if __name__ == '__main__':
    rand_int = random.randint(0, 100)
    print(f"in range of 0 - 100 = {rand_int}")

    rand_color = random.choice(["red", "green", "blue"])
    print(f'Random color = {rand_color}')
