class Product:

    def __init__(self, price, name, size):
        self.price = price
        self.name = name
        self.size = size

    def __str__(self):
        return "Product [price = " + str(self.price) + " UAH, description = " + str(self.name) + ", size = " + str(
            self.size) + " kg/liter(s)]"


class Client:

    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return "User: Имя - " + str(self.name + ", Фамилия - " + str(self.last_name) + ", телефон - " + str(
            self.phone) + "]")


class Order:

    def __init__(self, user, *goods):
        self.user = user
        self.goods = goods

    def summa(self):
        sum = 0
        for good in self.goods:
            sum = sum + good.price

    def __str__(self):
        result = " "
        for good in self.goods:
            result = result + str(good.name) + " : " + str(good.price) + " UAH\n"
        sum = 0
        for good in self.goods:
            sum = sum + good.price
        result = str(self.user) + '\n' + result + " Sum: " + str(sum) + " UAH"
        return result


thing_1 = Product(45, 'Латте', 0.75)
thing_2 = Product(56, ' Холодный чай', 1)
user_1 = Client('Ярослав', 'Гайдукевич', '0987777777')

order_1 = Order(user_1, thing_1, thing_2)
print(order_1)
