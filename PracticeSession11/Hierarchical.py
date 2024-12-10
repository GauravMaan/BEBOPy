class Vehicle:
    brand = ""
    model = ""
    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}"
class Car(Vehicle):
    def car_details(self):
        return f"{self.display_details()}"

class Bike(Vehicle):
    def bike_details(self):
        return f"{self.display_details()}"
car = Car()
car.brand = "Toyota"
car.model = "Camry"
print(car.car_details())

bike = Bike()
bike.brand = "Yamaha"
bike.model = "FZ"
print(bike.bike_details())