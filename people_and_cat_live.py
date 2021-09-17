from random import randint

from termcolor import cprint


class Сreation:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None




class Man(Сreation):

    def __init__(self, name):
        super().__init__(name=name)
        self.happiness = 10

    def __str__(self):
        return 'Житель - {}, Сытость - {}, Счастье - {}'.format(self.name, self.fullness, self.happiness)

    def play_dota(self):
        cprint('{} играл в доту'.format(self.name), color='blue')
        self.fullness -= 10

    def eat(self):
        cprint('{} поел'.format(self.name), color='green')
        self.fullness += 15

    def shopping(self):
        print('{} сходил в магазин'.format(self.name))
        self.house.food += 50
        self.house.cats_food += 50
        self.house.money -= 100
        self.fullness -= 10

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def cleaning(self):
        print('{} убрался в доме'.format(self.name))
        self.house.rubbish -= 40
        self.happiness += 20

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} въехал в дом'.format(self.name))

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.rubbish > 50:
            self.happiness -= 10
        dice = randint(1, 6)

        if self.fullness < 11:
            self.eat()
        elif self.house.food < 15 or self.house.cats_food < 15:
            self.shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.rubbish > 40:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()



class Cat(Сreation):

    def pear_wallpaper(self):
        print('{} драл обои'.format(self.name))
        self.house.rubbish += 10
        self.fullness -= 10

    def __str__(self):
        return 'Питомец - {}, Сытость - {}'.format(self.name, self.fullness)


    def go_into_house(self, house):
        self.house = house
        print('{} въехал в дом'.format(self.name))

    def sleep(self):
        print('{} спал'.format(self.name))
        self.fullness -= 10

    def eat(self):
        print('{} ел'.format(self.name))
        self.fullness += 10
        self.house.cats_food -= 10

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')

        dice = randint(1, 6)
        if self.fullness < 16:
            self.eat()

        elif dice == 1:
            self.eat()
        elif dice == 1:
            self.eat()
        else:
            self.pear_wallpaper()

class House:
    def __init__(self):
        self.food = 30
        self.cats_food = 30
        self.money = 50
        self.rubbish = 0

    def __str__(self):
        return 'В доме осталось еды - {}, кошачей еды - {}, денег - {}, мусора - {}'.format(
            self.food, self.cats_food, self.money, self.rubbish)


cityzens = [
    Man(name='Ахмед'),
    Man(name='Ибрагим'),
    Man(name='Мустафа')
]

cats = [
    Cat(name="Барсик"),
    Cat(name="Котяра"),
    Cat(name="Помойный кот")
]

sweet_home = House()

for cityzen in cityzens:
    cityzen.go_into_house(house=sweet_home)

for cat in cats:
    cat.go_into_house(house=sweet_home)


for day in range(1, 361):
    cprint('================ день {} =================='.format(day), color='yellow')
    for citisen in cityzens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citisen in cityzens:
        cprint(citisen, color='magenta')
    for cat in cats:
        cprint(cat, color='cyan')

    cprint(sweet_home, color='green')

