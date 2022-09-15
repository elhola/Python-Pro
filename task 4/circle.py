class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle height = {self.height}, width = {self.width}'

    def value(self):
        return self.height * self.width

    def __add__(self, other):
        return Rectangle(self.height + other.height, self.width + other.width)

    def __iadd__(self, other):
        self.height += other.height
        self.width += other.width
        return self

    def __rmul__(self, other):
        return other.value() * self.value()

    def __mul__(self, other):
        if not isinstance(self, int):
            return NotImplemented
        return Rectangle(self.height * other, self.width * other)

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __eq__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.height * self.width == other.height * other.width

    def __ne__(self, other):
        return self.value() != other.value()


r_1 = Rectangle(5, 4)
r_2 = Rectangle(5, 3)
r_3 = r_1.value() * 2
r_4 = r_1 + r_2

print(r_1)
print(f'square:', r_1.value())
print(r_2)
print(r_1 == r_2)
print(r_1 > r_2)
print(r_3)
print(r_4)
