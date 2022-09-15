import time


class MyDescriptor:
    def __set__(self, instance, value):
        file = open('Greeting.txt', 'a')
        file.write(f'{time.ctime()} name= {value}\n')
        file.close()
        self.name = value


class Greeting:
    name = MyDescriptor()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f' hi, my name is {Greeting.name.name}'


suz = Greeting('Suzune')
print(suz)