def infected(s):
    if not '1' in s:
        return 0
    splt = s.split('X')
    for i in range(len(splt)):
        if '1' in splt[i]:
            splt[i] = len(splt[i]) * '1'
    joyn = 'X'.join(splt)
    return 100 * joyn.count('1') / (joyn.count('0') + joyn.count('1'))



string = "01000000X000X011X0X"
print(infected(string))