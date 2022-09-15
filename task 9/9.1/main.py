count_func = 0


def function_decorator(ff):
    def counter(*args, **kwargs):
        global count_func
        count_func += 1
        return ff(*args, **kwargs)
    return counter


@function_decorator
def add_numbers(a, b):
    return a + b


print(add_numbers(1, 3))
print(add_numbers(3, 2))
add_numbers(2, 1)
print(f"Function called {count_func} times")
