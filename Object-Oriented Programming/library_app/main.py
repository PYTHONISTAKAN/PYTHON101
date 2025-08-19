from book import Book
from user import User
from library import Library

def main():
    # Create the library
    library = Library()

    # Create some books
    book1 = Book("1984", "George Orwell", "12345")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

    # Create a user
    user1 = User("Atakan", "u001")

    # Register books and user to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_user(user1)

    # Display current books and users
    library.list_books()
    library.list_users()

    # Borrow and return a book
    user1.borrow_book(book1)
    library.list_books()

    user1.return_book(book1)
    library.list_books()

if __name__ == "__main__":
    main()
