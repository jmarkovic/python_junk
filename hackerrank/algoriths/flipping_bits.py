def flip_bits_32(number_to_flip):
    return ~number_to_flip & 0xffffffff;

total_rows = int(input())

for i in range(0, total_rows):
    number = int(input())
    result = flip_bits_32(number)
    print(result)