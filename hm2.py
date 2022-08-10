
class Human:

    def __init__(self,surname, name, birthday):
        self.surname = surname
        self.name = name
        self.birthday = birthday


    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.birthday}'
    #def __str__(self):
    #    return 'Human: ' + 'name - {}, surname - {}, birthday - {}'.format(self.name, self.surname, self.birthday)

class Student(Human):
    '''
    describing a student
    фамилия, имя, средний балл и специальность
    ''' 
    def __init__(self,surname, name, birthday, gpa, speciality):
        super().__init__(surname, name, birthday)
        self.gpa = gpa
        self.speciality = speciality

    def __str__(self):
        return super().__str__()+ f',  {self.gpa}, {self.speciality}'

class Group:

    def __init__(self):
        self.students = []


    def add_student(self, new):
        self.students.append(new)

    def delete_student(self, student):
        self.students.remove(student)

    def BinarySearch_st(self, surname):
        first = 0
        last = len(self.students)-1
        index = -1
        st = None
        while (first <= last) and (index == -1):
            mid = (first+last)//2
            if surname[mid] == st:
                index = mid
            else:
                if st<surname[mid]:
                    last = mid -1
                else:
                    first = mid +1
                return index

    def __str__(self):
        result = ''
        for new in self.students:
            result = result + str(new) + ' \n              '
        return 'Student list: ' + result

thing_1 = Student('Максимов','Михаил',1999, 3.54,'економист')
thing_2 = Student('Иванов','Виктор',1997,  4.42,'пайтон прогр')
thing_3 = Student('Лоывв','Биба',1979, 5,'си++ прогр')
thing_4 = Student('Говыв','Рыы',2005, 4.8,'архитектура')
thing_5 = Student('Рвыов','Аба',2006, 3,'джава прогр')

group_1 = Group()
group_1.add_student(thing_1)
group_1.add_student(thing_2)
group_1.add_student(thing_3)
group_1.add_student(thing_4)
group_1.add_student(thing_5)

#x= Group
#x.BinarySearch_st(surname='Иванов')
print(group_1)
