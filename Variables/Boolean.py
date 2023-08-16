
if __name__ == "__main__":
    yes = False and True
    print(1, yes)

    yes = (1 == 1 and 2 == 1)
    print(2, yes)

    yes = (1 == 1 or 2 == 1)
    print(3, yes)

    yes = "test" == "testing"
    print(4, yes)

    yes = "test" != "testing"
    print(5, yes)

    yes = not (1 == 1 and 2 == 1)
    print(6, yes)
