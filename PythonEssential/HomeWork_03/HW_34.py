class Base:
    def __init__(self):
        pass

    def b_method(self):
        return 'Hello from Base'


class Child(Base):
    def __init__(self):
        Base.__init__(self)

    def c_method(self):
        return 'Hello from Child'


x = Child()
print(x.b_method())
print(x.c_method())
