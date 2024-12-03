class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")
animal1 = Animal("Lion")
animal2 = Animal("Eagle")
animal3 = Animal("Shark")
animal1.display_info()
animal2.display_info()
animal3.display_info()