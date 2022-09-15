class NotPrice(Exception):

    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return 'отрицательное значение'


while True:
    try:
        price = float(input('введите цену в грн: '))
        if price < 0:
            raise NotPrice(price)
        break
    except ValueError as err:
        print('только цифры')
    except NotPrice as err:
        print(err, ' = ', err.price)

print(price)
