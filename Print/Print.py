
if __name__ == '__main__':
    print(1)

    print(1, 2, 3)

    # "one", "two", "three" will be separated with ' '
    print("one", "two", "three")

    # "one", "two", "three" will be separated with '_'
    print("one", "two", "three", sep='_')

    # "one", "two", "three" will NOT be separated: separator - ''
    print("one", "two", "three", sep='')

    print()

    # "one", "two", "three" will printed each on the new line
    print("one", "two", "three", sep='\n')
