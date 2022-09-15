decorator_list = []


def reg_decorator(f):
    decorator_list.append(f)
    return f


@reg_decorator
class Firstclass:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass


el = Firstclass
print(el)
print(decorator_list)
