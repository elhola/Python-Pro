import abc


class PrimeCheck(abc.ABC):

    @abc.abstractmethod
    def is_prime(self):
        pass


class NumberCheck(PrimeCheck):
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
        return True


class Odd:
    def __init__(self, num):
        self.num = num

    def is_odd(self):
        if self.num % 2 != 0:
            return True
        return False


PrimeCheck.register(Odd)

num_1 = NumberCheck(14)
print(isinstance(num_1, PrimeCheck))

num_2 = Odd(3)
print(isinstance(num_2, PrimeCheck))
