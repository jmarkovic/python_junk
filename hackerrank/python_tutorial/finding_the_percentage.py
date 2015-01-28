# https://www.hackerrank.com/challenges/finding-the-percentage
from functools import reduce


def student_input():
    s_list = [elem for elem in input().split()]
    s_list[1] = float(s_list[1])
    s_list[2] = float(s_list[2])
    s_list[3] = float(s_list[3])
    return s_list


def avg_grade(s_list):
    return reduce(lambda a, x: a + x, s_list) / len(s_list)


student_num = int(input())
student_dict = {}
for i in range(student_num):
    s_info = student_input()
    name = s_info[0]
    del s_info[0]
    student_dict[name] = s_info

selected_student_name = input()
print("{0:.2f}".format(avg_grade(student_dict[selected_student_name])))