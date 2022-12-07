class Cola(object):
    def drink(self):
        print('Drink Cola')


class Sprite(object):
    def drink(self):
        print('drink sprite')


class Fact(object):
    def __init__(self, x):
        self.x = x

    def getObject(self):
        if self.x > 10:
            return Cola()
        else:
            return Sprite()
