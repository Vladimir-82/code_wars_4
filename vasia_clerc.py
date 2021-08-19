def tickets(people):
    '''Vasya - Clerk'''
    cassa = []
    if 25 not in people:
        return 'NO'
    for i in people:
        if i == 25:
            cassa.append(i)
        elif i == 50:
            if 25 in cassa:
                cassa.append(i)
                cassa.remove(25)
            else:
                return 'NO'
        elif i == 100:
            if 50 in cassa and 25 in cassa:
                cassa.append(i)
                cassa.remove(50)
                cassa.remove(25)
            elif cassa.count(25) >= 3:
                cassa.append(i)
                cassa.remove(25)
                cassa.remove(25)
                cassa.remove(25)
            else:
                return 'NO'

    return 'YES'

print(tickets([25, 25, 25, 25, 50, 100, 50]))