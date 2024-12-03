# class Library:
#     def __init__(self):
#         self.books = {}
#
#     def add_book(self, title, quantity):
#         if title in self.books:
#             self.books[title] += quantity
#         else:
#             self.books[title] = quantity
#         print(f"{quantity} copies of '{title}' added to the library.")
#
#     def borrow_book(self, title):
#         if title in self.books and self.books[title] > 0:
#             self.books[title] -= 1
#             print(f"You have borrowed '{title}'.")
#         else:
#             print(f"Sorry, '{title}' is unavailable or out of stock.")
#
#     def display_books(self):
#         if self.books:
#             print("Books available in the library:")
#             for title, quantity in self.books.items():
#                 print(f"'{title}' - {quantity} copies")
#         else:
#             print("No books available in the library.")
#
# # Example usage
# library = Library()
# library.add_book("Python Programming", 5)
# library.add_book("Data Structures", 3)
# library.display_books()
# library.borrow_book("Python Programming")
# library.display_books()