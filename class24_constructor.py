# The constructor ( __init__ method) is called when an object is created,
# allowing for initialization of attributes. Conversely, the destructor
# ( __del__ method) is called when an object is about to be destroyed.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"a new book titled {title} by {author}")

    def __del__(self):
        print(f"a book {self.title} was deleted")

my_book = Book("Hunger games", "William James")
print(my_book.title)
print(my_book.author)

del my_book