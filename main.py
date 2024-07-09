from library import Library
from book import Book
from member import Member

def main():
    library = Library("City Library")
    member1 = Member("Alice")
    member2 = Member("Bob")

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    library.register_member(member1)
    library.register_member(member2)

    library.issue_book(book1, member1)
    library.issue_book(book2, member2)

    library.display_books()
    library.display_members()

if __name__ == "__main__":
    main()
