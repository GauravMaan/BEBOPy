class Book:
    def __init__(self, title):
        self.title = title

    def __del__(self):
        print(f"The book '{self.title}' has been deleted.")
book = Book("Python Programming")
print(f"Created book: {book.title}")
del book