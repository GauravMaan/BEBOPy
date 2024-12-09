class Animal:
    def sound(self):
        raise NotImplementedError()
class Dog(Animal):
    def sound(self):
        return "Bhuu Bhuu"
class Cat(Animal):
    def sound(self):
        return "Meow Meow"
class Cow(Animal):
    def sound(self):
        return "Moo Moo"
def play_sound(animal):
    print(animal.sound())
dog = Dog()
cat = Cat()
cow = Cow()
play_sound(dog)
play_sound(cat)
play_sound(cow)