# was not able to test this, hackerrank module stopped working


def get_student():
    name = input("")
    grade = float(input(""))
    return [name, grade]


def second_lowest(a_list):
    smallest = 0
    second_smallest = 0
    for elem in a_list:
        if smallest == 0:
            smallest = elem
        if elem < smallest:
            smallest = elem

    for elem in reversed(a_list):
        if second_smallest == 0:
            second_smallest = elem
        if second_smallest > elem > smallest:
            second_smallest = elem

    return second_smallest


# total students to input
total_inputs = int(input())

# user input
students = []
for val in range(total_inputs):
    students.append(get_student())

students = sorted(students, key=lambda student: student[1])
grades = [student[1] for student in students]
second_lowest_grade = second_lowest(grades)
filtered_students = sorted([student for student in students if student[1] == second_lowest_grade])
for student in filtered_students:
    print(student[0])