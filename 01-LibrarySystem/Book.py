class Book():
    title = ""
    author = ""
    published_year = 0
    is_available = True

    def __init__(self):
        return
    
    def check_availability(self):
        if self.is_available:
            return f"{self.title} is Available"
        else:
            return f"{self.title} not Available"
        

# my_book = Book()
# my_book.title = "GOYT"
# my_book.is_available = False


# print(my_book.check_availability())