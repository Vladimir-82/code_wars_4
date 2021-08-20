import time


def sol_equa(n):
    '''Diophantine Equation'''
    out = []
    for y in range(n):
        x = (n + 4 * y ** 2)**0.5
        if str(x)[-2:] == '.0':
            res = x ** 2 - 4 * y ** 2
            if res == n:
                out.append([int(x), y])

    return sorted(out, reverse=True)


start = time.time()
print(sol_equa(90005))
finish = time.time()
print(finish - start)