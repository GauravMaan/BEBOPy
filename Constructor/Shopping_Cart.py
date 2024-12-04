# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#         print(f"{item} has been added to the cart.")
#
#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"{item} has been removed from the cart.")
#         else:
#             print(f"{item} not found in the cart.")
#
#     def display_items(self):
#         if self.items:
#             print("Items in the cart:")
#             for item in self.items:
#                 print(f"- {item}")
#         else:
#             print("The cart is empty.")
# cart = ShoppingCart()
# cart.add_item("Laptop")
# cart.add_item("Smartphone")
# cart.display_items()
# cart.remove_item("Laptop")
# cart.display_items()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to the cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def display_items(self):
        if self.items:
            print("Items in the cart:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("The cart is empty.")

def main():
    cart = ShoppingCart()
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Display items")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the name of the item to add: ")
            cart.add_item(item)
        elif choice == "2":
            item = input("Enter the name of the item to remove: ")
            cart.remove_item(item)
        elif choice == "3":
            cart.display_items()
        elif choice == "4":
            print("Exiting the shopping cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()