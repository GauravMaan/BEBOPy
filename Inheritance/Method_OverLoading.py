class A:
    def m(self, name=None):
        if name is not None:
            print("Hi " + name)
        else:
            x = 5
            y = 10
            print(x + y)

obj = A()
obj.m("Gaurav")
obj.m()