# class Cars:
#     def __init__(self, name, cid, model):
#         self.n = name
#         self.c = cid
#         self.m = model
#
#     def display(self):
#         print(self.n, self.c, self.m)
#
#     def __str__(self):
#         return (f"name={self.n} cid={self.c} model={self.m}")
#
#
# obj1 = Cars("Mustang", 1996, 196)
# obj1.display()
# print(obj1)
# del obj1.c #using del keyword for deleting the attribute from code
# print("obj is del",obj1.c)

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"Car Name: {self.name}, Model: {self.model}"

    def __del__(self):
        print(f"The object {self.name} has been deleted.")
car1 = Car("Mustang", 1965)
car2 = Car("Camaro", 2020)
print(car1)
print(car2)

# Delete car1
del car1

# Attempt to print deleted object will cause an error (uncomment to test)
# print(car1)