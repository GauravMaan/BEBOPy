class Person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def display(self):
        print(self.n,self.a)
obj1=Person("gaurav",23)
obj1.display()
