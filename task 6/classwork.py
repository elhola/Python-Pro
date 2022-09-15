class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Group:

    def __init__(self):
        self.__students = []

    def add_student(self, item: Student):
        self.__students.append(item)

    def __len__(self):
        return len(self.__students)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or len(self.__students) - 1
            step = item.step or 1

            return [self.__students[i] for i in range(start, stop + 1, step)]

        if isinstance(item, int):
            return self.__students[item]

        raise TypeError()


st_1 = Student('St_1')
st_2 = Student('St_2')
st_3 = Student('St_3')
st_4 = Student('St_4')
st_5 = Student('St_5')

group = Group()
group.add_student(st_1)
group.add_student(st_2)
group.add_student(st_3)
group.add_student(st_4)
group.add_student(st_5)

for student in group:
    print(student)

tmp = group[::2]
print(tmp, len(tmp))
