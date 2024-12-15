class Parrot:
    def speak(self):
        return "Squawk! I'm a parrot."
class Fish:
    pass
def describe_pet(pet):
    try:
        print(pet.speak())
    except AttributeError:
        print(f"The object of type {type(pet).__name__} does not have a 'speak' method.")
parrot = Parrot()
fish = Fish()

describe_pet(parrot)
describe_pet(fish)