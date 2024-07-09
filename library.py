from utils import print_separator
from book import Book
from member import Member

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def issue_book(self, book, member):
        if book in self.books:
            book.issued_to = member
            print(f"Book '{book.title}' issued to {member.name}")
        else:
            print(f"Book '{book.title}' is not available in the library.")

    def display_books(self):
        print("Books in library:")
        for book in self.books:
            print(f"- {book.title} by {book.author}")
        print_separator()

    def display_members(self):
        print("Members of library:")
        for member in self.members:
            print(f"- {member.name}")
        print_separator()
