def sol_equa(n):
    '''Diophantine Equation'''
    out = []
    x = n
    y = x - 1
    while x > 0:

        res = x ** 2 - 4 * y ** 2
        if res < 0:
            x -= 1
            y = x - 1

        elif res == n:
            out.append([x, y])

        y -= 1
        if y < 0:
            x -= 1
            y = x - 1
    return out

print(sol_equa(12))