from animals import Animal

class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed 

    def speak(self):
        return f"{self.name} neighs: Iihhaaa!"

    def gallop(self):
        return f"{self.name} is galloping at {self.speed} km/h!"

    def info(self):
        return super().info() + f", Speed: {self.speed} km/h"