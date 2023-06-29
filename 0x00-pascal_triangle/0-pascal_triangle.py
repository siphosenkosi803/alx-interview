#!/usr/bin/python3
'''this will return a pascal triangle'''


def pascal_triangle(n):
    '''
    will return a list of lists of integers representing
    a Pascal's triangle of a given integer
    '''
    lists = []
    if n == 0:
        return lists
    for h in range(n):
        lists.append([])
        lists[h].append(1)
        if (h > 0):
            for k in range(1, h):
                lists[h].append(lists[h - 1][k - 1] + lists[h - 1][k])
            lists[h].append(1)
    return lists
