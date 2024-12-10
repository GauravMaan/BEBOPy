class Person:
    def __init__(self, name, age):
        self._name = name        # Protected attribute (single underscore)
        self.__age = age         # Private attribute (double underscore)

    def get_age(self):
        return self.__age
p = Person("Gaurav", 23)
print(p._name)
print(p.get_age())
print(p._Person__age)