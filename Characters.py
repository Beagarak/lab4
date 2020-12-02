class Character:
    def __init__(self):
        self.health = 100
        self.armor = 0
        self.money = 16000
        self.height = 1
        self.speed = 2
        self.noise = 1

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


class SWAT(Character):
    swat_counter = 0
    def __init__(self):
        SWAT.swat_counter += 1
        if SWAT.swat_counter > 5:
            print('Игроков спецназа слишком много')
        else:
            super().__init__()
            self.weapon = 'SWAT'
            self.defuse_ability = 0
            print('Я - солдат, я не спал пять лет...')


    def defuse(self):
        if self.defuse_ability == 0:
            print('обезвреживаю бомбу, справлюсь за 10 сек')
        else:
            print('обезвреживаю бомбу, справлюсь за 5 сек')


class Terrorist(Character):
    def __init__(self):
        super().__init__()
        self.weapon = 'Ter'
        print('Бомбим,чувачки')

    def plant_bomb(self):
        print('Бомба установлена')


