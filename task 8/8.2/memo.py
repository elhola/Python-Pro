import time


def fibo_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_sequence(n - 1) + fibo_sequence(n - 2)


start_one = time.time()
print(fibo_sequence(20))
print("Время рекурсивной функции: ", time.time() - start_one)


def get_fibo(storage={}):
    def calculation(n):
        if n in storage:
            return storage[n]
        elif n == 0:
            storage[n] = 0
        elif n == 1:
            storage[n] = 1
        else:
            storage[n] = calculation(n - 1) + calculation(n - 2)
        return storage[n]

    return calculation


c = get_fibo()
start_two = time.time()
print(c(20))
print("Время мемоизации и замыкания: ", time.time() - start_two)
