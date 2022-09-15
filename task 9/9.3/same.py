def str_decorator(f):
    def save_to_file(arg):
        file = open(arg.__class__.__name__ + ".txt", "w")
        file.write(f(arg))
        file.close()
        return f(arg)

    return save_to_file


class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @str_decorator
    def __str__(self):
        return f"Parrot: Name - {self.name}, age - {self.age}"


Parrot_1 = Parrot("Kesha", 4)
print(Parrot_1)

