class MyDescriptor:
    def __init__(self, number):
        self.number = number

    def __get__(self, instance, owner):
        return self.number

    def __set__(self, instance_self, value):
        if not isinstance(value, int):
            raise AttributeError('can not change parameters')
        else:
            self.number = value

    def __delete__(self, instance_self):
        raise AttributeError('can not change parameters')


class Sample:
    name = MyDescriptor(100)

    def __str__(self):
        return f'{self.name} year'


a = Sample()
print(a)
a.name = 'bb'  # AttributeError
print(a)
