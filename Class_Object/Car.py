class Car:
    brand=""
    model=""
    def car_info(self,brand,model):
        print(f"Car Brand: {brand}, Model: {model}")
car1 = Car()
car2 = Car()
car3 = Car()
car1.car_info("Toyota", "Corolla")
car2.car_info("Tesla", "Model S")
car3.car_info("Ford", "Mustang")