

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = ['one', 'two', 'three']
    list3 = ['I', 'II', 'III', 'IV', 'V']

    for a, b in zip(list1, list2):
        print(a, " = ", b)

    print()

    for a, b, c in zip(list1, list2, list3):
        print(a, " = ", b, " = ", c)
