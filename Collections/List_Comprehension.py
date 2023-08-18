

if __name__ == "__main__":
    nums = [n for n in range(1, 6)]
    print(nums)

    nums = [1, 2, 3, 4, 5]
    squares = [n * n for n in nums]
    print(squares)

    odds = [n for n in nums if n % 2 == 1]
    evens = [n for n in nums if n % 2 == 0]
    print(odds)
    print(evens)
