class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(f"Brand: {self.brand}, Wheels: {Car.wheels}")
    def delete_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)
            print(f"Attribute '{attr_name}' has been deleted.")
        else:
            print(f"Attribute '{attr_name}' does not exist.")
car = Car("Tesla")
car.show()
car.delete_attribute("brand")
car.show()
car.delete_attribute("color")