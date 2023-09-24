from Library import Library
from Book import Book

# Create an instance of the Library class.
my_LIB = Library()

# Add at least three book objects to the library.
first_book = Book()
first_book.title = "Harry Potter"
first_book.author = "J.K"
first_book.published_year = 2023

second_book = Book()
second_book.title = "GOT"
second_book.author = "John Snow"
second_book.published_year = 2023


third_book = Book()
third_book.title = "Moonlight"
third_book.author = "Disney"
third_book.published_year = 2023


my_LIB.add_book(first_book)
my_LIB.add_book(second_book)
my_LIB.add_book(third_book)

# Display a list of available books in the library
print(my_LIB.list_available_books())

# Check out one of the books
my_LIB.check_out_book(second_book)

# Display the list of available books again.
print(my_LIB.list_available_books())

# Return the checked-out book
my_LIB.return_book(second_book)

# Display the list of available books once more
print(my_LIB.list_available_books())

my_LIB.check_out_book(third_book)
print(my_LIB.list_available_books())

my_LIB.check_out_book(third_book)

my_LIB.return_book(first_book)