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

    def search_books(self, search_term):
        """söker efteer böcker basserat på titel eller författare"""
        results = [book for book in self.books if search_term.lower() in book.titel.lower() or search_term.lower() in book.author.lower()]
        if not results:
            print(f"inga böcker hittades med söktermen '{search_term} '.")
        else:
            print(f"böcker som matchar '{search_term}': ")
            for index, book in enumerate(results, start=1):
                print(f"{index}. {book}")

    def remove_book(self,index):
        """Tar bort en bok baserat på dess index"""
        try:
            removed_book = self.books.pop(index - 1)
            print(f"'{removed_book.title}' har tagits bort från biblioteket.")
        except IndexError:
            print("ogiltig index. ingen bok togs bort")

    def clear_library(self):
        """tar bort alla böcker i biblioteket"""
        self.books.clear()
        print("alla böcker har tagits bort från biblioteket") 

# Exempel på användning:
b1 = Book("1984", "George Orwell", 1949)
b2 = Book("Brave New World", "Aldous Huxley", 1932)
b3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.view_books()
library.search_books("george")
library.remove_book(2)
library.view_books()
library.clear_library()
library.view_books()
