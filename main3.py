import settings



class Person:

    def __init__(self, surname, name):
        if not isinstance(surname, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'


class Student(Person):

    def __init__(self, surname: str, name: str, date_of_birth: str):
        super().__init__(surname, name)
        self.date_of_birth = date_of_birth


    def __eq__(self, other):
        return self.surname == other.surname and self.name == other.name and self.date_of_birth == other.date_of_birth


    def __str__(self):
        return f'{super().__str__()}; {self.date_of_birth}'

class MaxStudentsError(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}\n{super().__str__()}'

class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) >= settings.MAX_STUDENTS_IN_GROUP:
            raise MaxStudentsError('Too many student in group!')

        for item in self.students:
            if item == student:
                return -2

        self.students.append(student)

    def search(self, surname):
        for item in self.students:
            if item.surname.lower() == surname.lower():
                return item

        return -1

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.students))

st_1 = Student('Ivanov', 'Ivan', '12-12-12')
st_2 = Student('Ivanov1', 'Ivan1', '12-12-12')
st_3 = Student('Ivanov1', 'Ivan2', '12-12-12')
st_4 = Student('Ivanov', 'Ivan3', '12-12-12')


try:
    gr = Group('234234')
    gr.add_student(st_1)
    gr.add_student(st_2)
    gr.add_student(st_3)
    gr.add_student(st_4)
except (ValueError, MaxStudentsError) as err:
    print('Набір завершено', err)
print(gr.search('ivanov'))

