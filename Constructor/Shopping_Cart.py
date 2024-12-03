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