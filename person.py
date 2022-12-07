class Person(object):
    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls)

    def __init__(self):
        print('init')
        self.instance_method()

    def instance_method(self):
        pass
