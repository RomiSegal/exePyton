import abc
from abc import ABC, abstractmethod

class Animal (ABC):
    __name = ''
# __ = private
# without access its public

    def __init__(self):
        self.time = None

    def sleep(self, time=0):
        # self = this
        self.time = time
        print('sleep in hours:'+str(self.time))

    def makeSound(self, sound):
        self.sound = sound
        print(self.sound)

    @abc.abstractmethod
    def move(self):
        pass