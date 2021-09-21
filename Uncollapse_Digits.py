def Uncollapse_Digits(digits):
    '''
    Uncollapse Digits
    '''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    res = []
    slz = 0
    while digits:
        var = digits[:slz+1]
        if var in numbers:
            print(var)
            res.append(var)
            digits = digits[slz+1:]
            slz = 0
        else:
            slz += 1
    return ' '.join(res)


print(Uncollapse_Digits("ninethreesixthreenine"))