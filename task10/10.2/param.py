def add_text(string):
    def class_decorator(cls):
        def adder(*args, **name_args):
            new_instance = cls(*args, **name_args)
            return string + str(new_instance)

        return adder

    return class_decorator


@add_text("text ")
class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Parrot [name - {self.name}, age - {self.age}]"


par_1 = Parrot("Glasha", 4)
print(par_1)
