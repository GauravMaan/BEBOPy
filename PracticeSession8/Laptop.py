class laptop:
    def __init__(self,brand,model):
        self.b=brand
        self.m=model
    def specifications(self):
        print(f"Name of the laptop: {self.b}  Its Model is: {self.m}")
obj=laptop("Apple","M1")
obj.specifications()