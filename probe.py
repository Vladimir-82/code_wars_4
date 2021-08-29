
# import itertools
# def sum_arrangements(num):
#     '''
#     Sum of all numbers with the same digits
#
#     '''
#     tpl = itertools.permutations(str(num), len(str(num)))
#     s = 0
#     for i in tpl:
#         s += int(''.join(i))
#
#     return s
#
#
#
#
# print(sum_arrangements(1185))

def sum_arrangements(num):
    '''
    Sum of all numbers with the same digits

    '''
    k = 0
    for i in str(num):
        k += int(i)


    res = ''
    size = len(str(num))

    k = k * (size - 1)
    ost = k

    while size:
        num = k + ost
        num = str(num)
        if size == 1:
            res = num + res
            break
        res = num[-1] + res
        ost = int(num[0])
        size -= 1

    return int(res) - k





print(sum_arrangements(1185))