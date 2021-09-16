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
        print('{} играет в доту'.format(self.name))
        self.fullness -= 10

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} въехал в дом'.format(self.name))





class Cat(Сreation):

    def pear_wallpaper(self):
        print('{} дерёт обои'.format(self.name))
        self.house.rubbish += 10

    def go_into_house(self, house):
        self.house = house
        print('{} въехал в дом'.format(self.name))


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




