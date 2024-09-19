grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list=sorted(students)
print(student_list)
middle_ball={}
for student, grade_list in zip (student_list, grades):
    middle_ball[student]=sum(grade_list)/(len(grade_list))
print(middle_ball)
