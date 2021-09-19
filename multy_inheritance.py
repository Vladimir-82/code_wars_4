class Robot:


    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Робот класса {} модель {}'.format(self.__class__.__name__, self.model)

    def operation(self):
        print('Объект {} Робот активизируется'.format(self.model))

class CanFly:

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

class Dron(Robot, CanFly):
    def operation(self):
        super().operation()
        print('Робот умеет летать')

class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operation(self):
        super().operation()
        print('Робот {} умеет стрелять из {}'.format(self.model, self.gun))

rob_1 = Robot('робот-1')
print(rob_1)
rob_1.operation()

rob_2 = Dron('робот-2')
print(rob_2)
rob_2.operation()

rob_3 = WarRobot('робот-3', 'бластер')
print(rob_3)
rob_3.operation()