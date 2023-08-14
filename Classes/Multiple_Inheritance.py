class Value:

    def __init__(self, val):
        self.value = val

    def info(self):
        print(self.value)


class Description:

    def __init__(self, descr):
        self.description = descr

    def info(self):
        print(self.description)


class ComplexObject(Value, Description):

    def __init__(self, value, description):
        Value.__init__(self, value)
        Description.__init__(self, description)

    def info(self):
        print(f'ComplexObject({self.value}, {self.description})')


if __name__ == "__main__":
    obj = ComplexObject("Some text", 123)
    obj.info()
    