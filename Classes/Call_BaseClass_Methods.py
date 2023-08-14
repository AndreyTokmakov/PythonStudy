class Base:
    def info(self):
        print('Base class info() called ')


class Derived(Base):

    def info(self):
        super().info()
        print('Derived class info() called ')


if __name__ == "__main__":
    d = Derived()
    d.info()
