from animals import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} is barking."
    
    def fetch(self):
        return f"{self.name} caught the ball."
    
    def info(self):
        return super().info() + f", Breed: {self.breed}"