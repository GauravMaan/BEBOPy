class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
animal = Animal()
dog = Dog()
cat = Cat()
print(isinstance(animal, Animal))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Cat))