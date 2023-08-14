'''
    while [condition]:
        ---- do smth ----

    'while' will execute while [condition] is True
'''

if __name__ == '__main__':

    counter = 0
    while counter < 5:
        print(counter, end=' ')
        # if we forget to increment counter ---> we will end up with eternal loop
        counter = counter + 1

    print()

    counter = 0
    while True:  # <--- True = eternal loop
        # counter becomes greater than 5 --> stop the loop
        if counter >= 5:
            break

        print(counter, end=' ')

        # if we forget to increment counter ---> we will end up with eternal loop
        counter = counter + 1
