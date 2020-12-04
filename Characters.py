import Weapon
from Weapon import weapon_list


class Character:
    def __init__(self):
        self.health = 100
        self.armor = 0
        self.money = 6000
        self.height = 1
        self.speed = 2
        self.noise = 1
        self.ammunition = 0

    def moving(self):
        if self.height == 0.5:
            print('Присел и крадусь к противнику')
        elif self.noise == 0:
            print('Kрадусь')
        else:
            print('Бегу')

    def sit(self):
        self.height = 0.5
        self.speed = 1
        self.noise = 0
        print('так меня не видно из-за укрытия')

    def stand(self):
        self.height = 1
        self.speed = 2
        self.noise = 1
        print('ничто меня не остановит ')

    def sneak(self):
        self.speed = 1
        self.noise = 0
        print('надеюсь, меня не заметят')

    def voice_command(self, number):
        comands_list = ['да', 'нет', 'пойдем', 'стой здесь']
        print(comands_list[number])

    def buy_weapon(self):
        print('Выберите оружие')
        for item in weapon_list:
            print(f'{item.name} стоит {item.cost}')
        choice = input('введите название оружия\n')
        for item in weapon_list:
            if choice == item.name:
                self.money -= item.cost
                self.ammunition = item


    def shooting(self, aim):
        if self.ammunition == 0:
            print('надо купить оружие')
        else:
            self.ammunition.shot()
            aim.health -= self.ammunition.damage


class SWAT(Character):
    def __init__(self):
        super().__init__()
        self.weapon = 'SWAT'
        self.defuse_ability = 0
        print('Я - солдат, я не спал пять лет...\n')

    def defuse(self):
        if self.defuse_ability == 0:
            print('обезвреживаю бомбу, справлюсь за 10 сек')
        else:
            print('обезвреживаю бомбу, справлюсь за 5 сек')


class Terrorist(Character):
    def __init__(self):
        super().__init__()
        self.weapon = 'Ter'
        print('Бомбим,чувачки\n')

    def plant_bomb(self):
        print('Бомба установлена')


# a = SWAT()
# t = Terrorist()
# a.buy_weapon()
# # print(a.money)
# # print(a.ammunition)
# a.shooting(t)
# # print(t.health)