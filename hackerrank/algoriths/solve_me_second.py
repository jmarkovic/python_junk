def sum_two_numbers(a, b):
    return a + b;

total_rows = int(input())

for i in range(0, total_rows):
    first_number, second_number = input().split()
    first_number, second_number = int(first_number), int(second_number)
    result = sum_two_numbers(first_number, second_number)
    print(result)