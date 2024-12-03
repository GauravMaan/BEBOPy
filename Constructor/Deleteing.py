class employee:
    def __init__(self, name, eid, sal):
        self.n = name
        self.e = eid
        self.s = sal

    def display(self):
        print(self.n, self.e, self.s)

    def __str__(self):
        return (f"name={self.n} eid={self.e} sal={self.s}")


obj1 = employee("gaurav", 9000, 8989)
obj1.display()
print(obj1)
del obj1.e #using del keyword for deleting the attribute from code
print(obj1.e)