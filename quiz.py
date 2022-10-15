"""
Warm up challenge of the day.
"""

int_list = []


def involute(num):
    number = num ** 2
    for i in range(1, number + 1):
        int_list.append(i)
    return i


print_grid(involute(5))
