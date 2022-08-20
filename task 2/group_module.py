import student_module
import settings
import exeption_module


class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student: student_module.Student):
        if len(self.students) >= settings.MAX_STUDENTS_IN_GROUP:
            raise exeption_module.MaxStudentsError('Too many student in group!')

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
