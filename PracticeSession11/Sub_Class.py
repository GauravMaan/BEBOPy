# Base class
class Animal:
    def speak(self):
        print("Animals make different sounds")
class Dog(Animal):
    def speak(self):
        print("Bark!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
class Vehicle:
    def start(self):
        print("Vehicle started")
print( issubclass(Dog, Animal))
print( issubclass(Cat, Animal))
print( issubclass(Vehicle,Animal))