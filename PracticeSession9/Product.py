class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def discounted_price(cls, name, dis_price, dis_per):
        original_price = dis_price / (1 - dis_per / 100)
        return cls(name, round(original_price, 2))
    def display(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")
product1 = Product("Laptop", 1200)
product1.display()
product2 = Product.discounted_price("Smartphone", 800, 20)
product2.display()