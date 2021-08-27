def Irreducible_Sum_of_Rationals(lst):
    '''
    Irreducible Sum of Rationals
    '''
    if not lst:
        return None
    up = []
    down = []
    for i in lst:
        up.append(i[0])
        down.append(i[-1])


    dev = max(down)

    counter = 0

    while True:
        if not dev % down[counter]:
            counter += 1
        else:
            dev += 1
            counter = 0
        if counter == len(down):
            break
    i = 0
    while True:
        if i == len(down):
            break
        num = dev//down[i]
        up[i] = up[i] * num
        i += 1
    return [sum(up), dev] if sum(up) % dev else sum(up) // dev

print(Irreducible_Sum_of_Rationals([]))