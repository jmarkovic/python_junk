def check_list_value_sum(checked_list, sum_value):
    '''
        Returns True if sum of list values
        is equal to sum_value
    '''
    return sum(checked_list) == sum_value


def build_lists(x, y, z):
    '''
        Builds a list containing lists with 3 elements.
    '''
    a_list = []
    for X in range(x + 1):
        for Y in range(y + 1):
            for Z in range(z + 1):
                a_list.append([X, Y, Z])
    return a_list


# take values from STDIN
coords = (int(input()), int(input()), int(input()))
should_not_sum = int(input())

a_list = [b_list for b_list in build_lists(coords[0], coords[1], coords[2]) if not check_list_value_sum(b_list, should_not_sum)]
print(a_list)