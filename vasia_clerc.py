def tickets(people):
    '''Vasya - Clerk'''
    cassa = []
    if 25 not in people:
        return 'NO'
    for i in people:
        if i == 25:
            cassa.append(i)
        else:
            stop = 1
            while stop <= len(cassa):
                change = cassa[:stop]
                if sum(change) == i - 25:
                    cassa = cassa[stop:]
                    cassa.append(i)
                    change = []
                    break
                else:
                    stop += 1
                    if stop > len(cassa):
                        return 'NO'

    return 'YES'



print(tickets([25, 25, 25, 25, 50, 100, 50]))