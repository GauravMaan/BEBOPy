class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")

print(animal.name)
print(dog.name, dog.breed)