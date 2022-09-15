class Product:

    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


class Customer:

    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'


class Cart:

    def __init__(self, customer: Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.products):
            res += f'\t{item} x {self.quantities[index]} = {item.price * self.quantities[index]} грн.\n'

        res += f'Total price: {self.total()} грн.'

        return res

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.products):
                return self.products[index]
            else:
                raise IndexError()

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.products) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            temp_product_list = []
            if start < 0 and stop >= len(self.products):
                raise IndexError()
            for i in range(start, stop, step):
                temp_product_list.append(self.products[i])
            return temp_product_list

        raise TypeError

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return ProductIterator(self.products)


class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration()
        temp = self.products[self.index]
        self.index += 1
        return temp


pr_1 = Product('banana', 20)
pr_2 = Product('apple', 21)
pr_3 = Product('orange', 22)

customer_1 = Customer('Ivan', 'Ivanov', '123456789')
customer_2 = Customer('Ivan', 'Petrov', '223456789')

order_1 = Cart(customer_1)
order_2 = Cart(customer_2)

order_1.add_product(pr_1, 2.5)
order_1.add_product(pr_2, 3)
order_1.add_product(pr_1, 2)
order_2.add_product(pr_1, 1)
order_2.add_product(pr_2, 1)
order_2.add_product(pr_3, 1)

print(order_1)
print(order_2)
