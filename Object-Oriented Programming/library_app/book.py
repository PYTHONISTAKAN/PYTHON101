class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} - ISBN: {self.isbn} ({'Available' if self.is_available else 'Not Available'})"
