class Thing:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = []

    def __str__(self):
        return f'{self.name},{self.price} +\n'.join(map(str, self.th))

class ThingError(Exception):
    """
    класс для отрицательных чисел
    """
    def __init__(self, th):
        super().__init__()
        self.th = th

    def __str__(self):
        return f'введите число больше нуля'

th_1 = Thing.th('вода', 32)
th_2 = Thing.th('сок', -43)
th_3 = Thing.th('торт', 265)
th_4 = Thing.th('бананы', 77)

try:
    th = int(input('введите цену в грн: '))
    if th < 0:
        raise ThingError(th)
except ValueError as err:
    print(f'текст запрещен')
except ThingError as err:
    print(err, f', ошибка!')
else:
    print(f'все ок')

print(th)