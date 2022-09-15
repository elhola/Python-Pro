class MetaToFile(type):
    def __new__(class_type, class_name, super_classes, class_atr):
        field_list = []
        for atr in class_atr:
            field_list.append(atr)
        file = open("MetaToFile.txt", "w")
        file.write(class_name + " - " + str(field_list))
        file.close()
        return type.__new__(class_type, class_name, super_classes, class_atr)


class Cat(metaclass=MetaToFile):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat [name = {self.name}, age = {self.age}]"
