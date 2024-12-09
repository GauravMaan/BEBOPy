class Animal:
    print("Animal Sound")
class Dog(Animal):
    def make_sound(self):
        print("Bhauu Bhauu")
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
class Cow(Animal):
    def make_sound(self):
        print("Moo Moo")
dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()