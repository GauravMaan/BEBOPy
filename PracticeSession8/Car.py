# class car:
#     def __init__(self,make,model,year):
#         self.Make=make
#         self.Model=model
#         self.Year=year
#     def display_info(self):
#         print(self.Make,self.Model,self.Year)
#     def start_engine(self):
#         print("Engine is starting")
# obj=car("Honda","i20","1996")
# obj.display_info()
# obj.start_engine()
class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(f"Brand: {self.brand}, Wheels: {Car.wheels}")
car1 = Car("Toyota")
car2 = Car("Honda")
car1.show()
car2.show()
