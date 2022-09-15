class Mydescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance_self, value):
        raise AttributeError('can not change parameters')

    def __delete__(self, instance_self):
        raise AttributeError('can not change parameters')


class Sample:
    name = Mydescriptor('Suzune')

    def __str__(self):
        return f'{self.name} hello'


a = Sample()
print(a)
