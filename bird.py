from animal import Animal

class Bird(Animal):
    def __init__(self, km):
        super().__init__()
        self.km = km

    def fly(self):
        print('I am flying ', self.km, ' km')

    def birdMakeSound(self):
        super().makeSound('switz switz')

    def move(self):
        print('bird move')
