import math


class Drop:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        if not isinstance(a, int):
            raise TypeError()
        if not isinstance(b, int):
            raise TypeError()
        if not b:
            raise ZeroDivisionError()

    @property
    def a(self):
        tmp = math.gcd(self.__a, self.__b)
        self.__a = self.__a // tmp
        self.__b //= tmp
        return self.__a

    @property
    def b(self):
        tmp = math.gcd(self.__a, self.__b)
        self.__a //= tmp
        self.__b //= tmp
        return self.__b

    def __str__(self):
        if self.a == 0:
            return f'0'
        elif self.b == 1:
            return f'{self.a}'
        elif self.a == self.b:
            return f'{self.a} // {self.b}'

        return f'{self.a} / {self.b}'

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __add__(self, other):

        if isinstance(other, Drop):
            b = self.__b * other.__b
            a = other.__b * self.__a + self.__b * other.__a

            return Drop(a, b)

    def __sub__(self, other):
        return Drop((self.a * other.b - other.a * self.b), self.b * other.b)

    def __mul__(self, other):
        return Drop(self.a * other.a, self.b * other.b)


x = Drop(1, 2)
y = Drop(2, 3)
d = Drop(1, 3)
b = x + y + d
print(b)
