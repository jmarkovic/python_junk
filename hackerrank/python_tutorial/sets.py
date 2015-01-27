# https://www.hackerrank.com/challenges/sets


def raw_input_to_set(raw_input):
    return set(map(int, raw_input.split()))


input()
a_set_raw_input = input()
input()
b_set_raw_input = input()

a_set = raw_input_to_set(a_set_raw_input)
b_set = raw_input_to_set(b_set_raw_input)

symmetric_difference = sorted([elem for elem in a_set.symmetric_difference(b_set)])

for i in symmetric_difference:
    print(i)