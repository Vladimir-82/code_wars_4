def Uncollapse_Digits(digits):
    '''
    Uncollapse Digits
    '''
    res = []
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in numbers:
        if i in digits:
            print(digits.find(i))



print(Uncollapse_Digits("ninethreesixthreenine"))