def tower_builder(n):
    'Build Tower'

    res = []
    size = 2 * n - 1
    for i in range(1, n + 1):

        var = 2 * i - 1
        res.append(((size - var) // 2) * ' ' + var * '*' + ((size - var) // 2) * ' ')
    return res

print(tower_builder(6))