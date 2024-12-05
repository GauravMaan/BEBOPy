class Person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def display(self):
        print(f"Name of person: {self.n}   Age of the person: {self.a}")
obj1=Person("gaurav",23)
obj2=Person("vivek",23)
obj1.display()
obj2.display()
