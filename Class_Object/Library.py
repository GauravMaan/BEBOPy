class Library:
    Total_book = 0

    def lib(self, count):
        Library.Total_book += count
        print(Library.Total_book)
library = Library()
library.lib(3)
library.lib(6)