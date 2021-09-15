import random

SUBJ = ['condoms', 'chocolate', 'water', 'whisky', 'phone', 'pm3', 'dildo', 'ass plagin']

class BackPack:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        self.content = []

    def add(self, subject):
        if subject not in self.content:
            print('В рюкзак ' + self.name + ' положили:', subject)
            self.content.append(subject)

    def inspect(self):
        print('В рюкзаке: ', self.content)

    def __str__(self):
        return 'В рюкзаке ' + self.name + ': ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


    def __eq__(self, other):
        return self.content == other.content


    def __add__(self, other):
        new_backpack = BackPack('Новый', 2)
        new_backpack.content.extend(self.content)
        new_backpack.content.extend(other.content)
        return new_backpack



my_backpack = BackPack('Вова', 4)

wives_backpack = BackPack('Оля', 3)



while True:

    if len(my_backpack.content) < my_backpack.volume:
        my_backpack.add(random.choice(SUBJ))


    if len(wives_backpack.content) < wives_backpack.volume:
       wives_backpack.add(random.choice(SUBJ))


    if len(my_backpack.content) == my_backpack.volume and \
            len(wives_backpack.content) == wives_backpack.volume:
                print('Рюкзаки заполнены')
                break

print(my_backpack)
print(wives_backpack)

if my_backpack == wives_backpack:
    print('we are so once')
else:
    print('we are difference')


new = my_backpack + wives_backpack
print(new)







