def Uncollapse_Digits(digits):
    '''
    Uncollapse Digits
    '''
    res = []
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in numbers:
        if i in digits:
            res.append(i)
    print(res)


print(Uncollapse_Digits("ninethreesixthree"))