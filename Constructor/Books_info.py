class Book:
    def __init__(self,name,author):
        self.n=name
        self.a=author
    def dispaly(self):
        print(self.n,self.a)
    def __str__(self):
        return (f"Book Name is :{self.n},Author: {self.a}")
obj1=Book("How to become Don in 2 Days","Vivek")
obj1.dispaly()
print(obj1)