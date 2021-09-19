def encrypt_this(text):
    '''Encrypt this!'''
    if text == '':
        return ''
    res = []
    splt = text.split(' ')
    for i in splt:
        if len(i) > 2:
            var = i[0] + i[-1] + i[2:-1] + i[1]
        else:
            var = i
        res.append(str(ord(var[0])) + var[1:])

    return ' '.join(res)

print(encrypt_this("Why can we not all be like that wise old bird"))


'87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri'
"87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"