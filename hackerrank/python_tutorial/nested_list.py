def get_student():
    return [input(), float(input())]

total_inputs = int(input())

students = []
for val in range(total_inputs):
    students.append(get_student())

sorted_students = sorted(students, key=lambda student: student[1])
sorted_student_names = sorted(student[0] for student in sorted_students if student[1] == sorted_students[0][1])
for st in sorted_student_names:
    print(st)