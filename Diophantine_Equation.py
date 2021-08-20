import time


def sol_equa(n):
    '''Diophantine Equation'''
    out = []
    for y in range(n):
        x = (n + 4 * y ** 2)**0.5
        x = int(x)
        res = x ** 2 - 4 * y ** 2
        if res == n:
            out.append([x, y])
        # if res > n:
        #     break
    return out


start = time.time()
print(sol_equa(90005))
finish = time.time()
print(finish - start)