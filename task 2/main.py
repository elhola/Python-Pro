import student_module
import group_module
import exeption_module


st_1 = student_module.Student('Ivanov', 'Ivan', '12-12-12')
st_2 = student_module.Student('Ivanov1', 'Ivan1', '12-12-12')
st_3 = student_module.Student('Ivanov1', 'Ivan2', '12-12-12')
st_4 = student_module.Student('Ivanov', 'Ivan3', '12-12-12')

try:
    gr = group_module.Group('Group 1')
    gr.add_student(st_1)
    gr.add_student(st_2)
    gr.add_student(st_3)
    gr.add_student(st_4)
except (ValueError, exeption_module.MaxStudentsError) as err:
    print('Набір завершено', err)
print(gr)
