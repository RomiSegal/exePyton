from animal import Animal

class Dog(Animal):
    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print('dog run km:' + str(self.km))

    def dogMakeSound(self):
        super().makeSound('av av')

    def move(self):
        print('dog move')