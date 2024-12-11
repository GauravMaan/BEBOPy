class Product:
    def __init__(self, price, stock):
        if price >= 0 and stock >= 0:
            self.__price = price
            self.__stock = stock
        else:
            raise ValueError("Price and stock must be non-negative.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Price cannot be negative.")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock >= 0:
            self.__stock = new_stock
        else:
            raise ValueError("Stock cannot be negative.")

    def display_product(self):
        print(f"Price: {self.__price}, Stock: {self.__stock}")
product = Product(100, 50)
product.display_product()
product.price = 120
product.stock = 40
product.display_product()