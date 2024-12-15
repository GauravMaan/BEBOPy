class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, name, max_speed, num_doors):
        super().__init__(name, max_speed)
        self.num_doors = num_doors
car = Car("Sedan", 180, 4)
print(f"Name: {car.name}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Number of Doors: {car.num_doors}")