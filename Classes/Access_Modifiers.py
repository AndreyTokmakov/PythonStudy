
class SomeTestClass:

    def __init__(self):
        self.username = "SomeTestName"
        self.__password = "12345"

    def public_info(self):
        self.__private_info()

    def __private_info(self):
        print('Some private information about the class')




if __name__ == "__main__":
    obj = SomeTestClass()

    obj.public_info()

    # obj.__private_info()

    print(f'Username : {obj.username}')
    # print(f'Password : {obj.__password}')
