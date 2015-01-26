def utopian_tree_height(cycle, height):
    '''
        Calculates the height of utopian tree for
        each cycle. If the cycle is an odd number,
        height is doubled. When the cycle is even
        numher, 1 is added to height.

        Returns: int -- height after cycle is applied
    '''

    'print("cycle -> {0}; height -> {1}".format(cycle, height))'
    if cycle % 2 == 1:
        height = height * 2
    else:
        height = height + 1

    return height


total_entries = int(input())

for entry in range(0, total_entries):
    max_cycles = int(input())
    height = 1
    for cycle in range(0, max_cycles):
        height = utopian_tree_height(cycle + 1, height)

    print (height)