from Characters import Terrorist, SWAT
class Gun:
    left_bullet = 0
    def shot(self, aim):
        if self.bullets_at_chamber < 0:
            print('ничего не происходит')
        else:
            self.bullets_at_chamber -= self.bullet_per_shot
            self.all_bullets -= self.bullet_per_shot
            print('Бах')
            print(f'Осталось {self.bullets_at_chamber} патронов')
            return aim.health - self.damage

    def reload(self):
        self.all_bullets -= Gun.left_bullet
        print('*Звук перезарядки*')
        print(f'Еще есть {self.all_bullets} патронов')

class Rifle(Gun):
    def __init__(self):
        self.damage = 30
        self.bullets_at_chamber = 30
        self.bullet_per_shot = 5
        self.all_bullets = 120
        self.cost = 2700


class Machinegun(Rifle):
    def __init__(self):
        super().__init__()
