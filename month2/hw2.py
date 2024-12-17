class Hero:
    def __init__(self, name = "john doe", hp = 100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp +=10
        return f'{self.name} heals hp +10, current hp is {self.hp}'

    def actions(self):
        return f'{self.name} doing basic things'

    def status(self):
        return f'Name:{self.name}\n Health:{self.hp}'


hero=Hero()
print(hero.status())
print(hero.actions())


class Warrior(Hero):

    def __init__(self, name = "<NAME>", hp = 100, st = 100):
        super().__init__(name, hp)
        self.st = st



    def attack(self):
        if self.st >= 10:
            self.st -=10
            return f'{self.name} turning into diamond'
        else:
            return f"{self.name} doesn't have enough stamina"

    def charge(self):
        if self.st >= 20:
            self.st -=20
            self.hp += 50
            return f"{self.name} use charge, hp increase +50. The rest of the stamina is {self.st}"
        else:
            return f"{self.name} doesn't have enough stamina"

    def status(self):
        return f'{super().status()}, Stamina:{self.st}'


hero_warrior = Warrior('<Roblox>', 100, 100)
# print(hero_warrior.rest())
print(hero_warrior.actions())
print(hero_warrior.status())
print(hero_warrior.charge())

class Mage(Hero):
    def __init__(self, name = "<NAME>", hp = 100, mana = 100):
        super().__init__(name, hp)
        self.mana = mana

    def rest(self):
        self.mana += 10
        return f'{self.name} replenishes mana +10 {self.mana}'


    def teleport(self):
        if self.mana >= 30:
            self.mana -= 30
            return f'{self.name} telepor. Current mana is {self.mana}'

    def attack(self):
         if self.mana >= 10:
             self.mana -= 10
             return f'{self.name} spells fire ball'
         else:
             return f"{self.name} doesn't have enough mana"

    def actions(self):
        old_actions = super().actions()
        attack = self.attack()
        return f'{old_actions} {attack}'

    def status(self):
        return f' {super().status()} Mana:{self.mana}'


hero_mage = Mage('<Rudeus>', 100, 1000)
print(hero_mage.actions())
print(hero_mage.status())
print(hero_mage.teleport())


class Archer(Hero):
    def __init__(self, name = "<NAME>", hp = 100, arrows = 25, precision = 100):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision


    def rest(self):
        self.precision += 15
        return f'{self.name} rest, current precision is {self.precision}'

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 50:  # Пример успешной атаки, если точность больше 50
                print(f"{self.name} shoot perfectly. Current arrow: {self.arrows}")
            else:
                print(f"{self.name} miss! Current arrow: {self.arrows}")
        else:
            print(f"{self.name} doesnt have enough arrows")
    def status(self):
        return f'{super().status()} Arrows:{self.arrows}'


hero_archer = Archer(name = "<zenit>", hp = 100, arrows = 25, precision = 45)
print(hero_archer.attack())
print(hero_archer.status())
#checking
# Проверка наследования
print(isinstance(hero_warrior, Hero))  # True
print(isinstance(hero_mage, Hero))  # True
print(isinstance(hero_archer, Hero))  # True
print(isinstance(hero, Warrior))  # False
print(isinstance(hero, Mage))  # False
print(isinstance(hero, Archer))  # False
