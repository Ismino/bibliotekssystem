class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Lägger till ny bok i biblioteket"""
        self.books.append
        print(f"'{book.title}' har lagts till i biblioteket. ")

    def view_books(self):
        """ visar alla böcker i biblioteket"""
        if not self.books:
            print("Biblioteket är tomt")
        else:
            print("Böcker i biblioteket.")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    