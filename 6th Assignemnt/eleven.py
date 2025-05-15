class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()


    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1


book1 = Book("Harry Potter ")
book2 = Book("Silent Therapist")               

print("Total books created:",Book.total_books)