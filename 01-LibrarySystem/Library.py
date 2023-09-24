class Library():
    name = "Iggy LIB"
    books = []

    def __init__(self):
        return
    
    def add_book(self, book):
        self.books.append(book.title)

    def check_out_book(self, title):
        if title.is_available:
            title.is_available = False
            # Remove book for list
            self.books.pop(self.books.index(title.title))
        else:
            print(f"{title.title} is not available, so you cannot check it out")

    def return_book(self, title):
        if title.is_available == False:
            title.is_available = True
            self.books.append(title.title)
        else:
            print(f"{title.title} is available, you cannot return it")

    def list_available_books(self):
        print(self.books)
        