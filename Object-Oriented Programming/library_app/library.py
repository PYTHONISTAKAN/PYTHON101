class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered in the system.")

    def list_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)

    def list_users(self):
        print("\n--- Registered Users ---")
        for user in self.users:
            print(user)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"No book found with title: {title}")
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print(f"No user found with ID: {user_id}")
        return None
