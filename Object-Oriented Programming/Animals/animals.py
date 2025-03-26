class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"Animals make sounds."
    
    def info(self):
        return f"Animal's name is {self.name} and its age is {self.age}."
    
