# import itertools
# def sum_arrangements(num):
#     tpl = list(itertools.permutations(str(num), len(str(num))))
#     summory = []
#     summ = ''
#     for i in tpl:
#         for j in i:
#             summ += j
#     while summ:
#         summory.append(summ[:len(str(num))])
#         summ = summ[len(str(num)):]
#
#     res = sum([int(i) for i in summory])
#
#     return res
#
#
# print(sum_arrangements(1185))

import itertools
def sum_arrangements(num):
    '''
    Sum of all numbers with the same digits

    '''
    tpl = itertools.permutations(str(num), len(str(num)))
    s = 0
    for i in tpl:
        s += int(''.join(i))

    return s




print(sum_arrangements(1185))