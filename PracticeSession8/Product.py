class Product:
    discount = 0.0
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price * (1 - Product.discount)
    @classmethod
    def set_discount(cls, discount_percentage):
        if 0 <= discount_percentage <= 1:
            cls.discount = discount_percentage
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 800)
Product.set_discount(0.2)
print("\nPrices with 20% discount:")
print(f"{product1.name}: ${product1.get_price():.2f}")
print(f"{product2.name}: ${product2.get_price():.2f}")