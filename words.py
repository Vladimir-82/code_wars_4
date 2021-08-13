def remove_duplicate_words(s):
    "Remove duplicate words"
    splt = s.split(' ')
    res = []
    for i in splt:
        if i not in res:
            res.append(i)
    return ' '.join(res)

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
