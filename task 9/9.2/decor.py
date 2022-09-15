function_list = []


def decorator(f):
    function_list.append(f)
    return f


@decorator
def mul(a, b):
    return a * b


print(function_list)
