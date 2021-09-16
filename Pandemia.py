def infected(s):
    res = ''
    splt = s.split('X')
    for i in splt:
        if '1' in i:
            res += len(i) * '1'
        else:
            res += i
    return res




string = "01000000X000X011X0X"
print(infected(string))