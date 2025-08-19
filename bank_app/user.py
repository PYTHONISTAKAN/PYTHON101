import random

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = self.generate_id()

    def generate_id(self):
        return random.randint(1000, 9999)

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, ID: {self.id}")