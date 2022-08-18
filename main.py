class NotDrop(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"ошибка: знаменатель не может быть меньше числителя"


class Drop:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a < self.b:
            return f'{self.a}'"/"f'{self.b}'
        raise NotDrop

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __add__(self, other):
        return Drop((self.a * other.b + other.a * self.b), self.b * other.b)

    def __sub__(self, other):
        return Drop((self.a * other.b - other.a * self.b), self.b * other.b)

    def __mul__(self, other):
        return Drop(self.a * other.a, self.b * other.b)


dr_1 = Drop(5, 13)
dr_2 = Drop(1, 4)

print(dr_1)
print(dr_2)

print(dr_1 == dr_2)
print(dr_1 > dr_2)
print(dr_1 < dr_2)
print(dr_1 + dr_2)
print(dr_1 - dr_2)
print(dr_1 * dr_2)
