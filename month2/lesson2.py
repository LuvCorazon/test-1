class Hero:
    def __init__(self, name = "john doe", hp = 100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp +=10
        return f'{self.name} heals hp +10, current hp is {self.hp}'

    def actions(self):
        return f'{self.name} doing basic things'

hero = Hero('<Ichigo>', 100)
# print(hero.rest())
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



hero_warrior = Warrior('<Roblox>', 100, 100)
# print(hero_warrior.rest())
print(hero_warrior.actions())


class Mage(Hero):
    def __init__(self, name = "<NAME>", hp = 100, mana = 100):
        super().__init__(name, hp)
        self.mana = mana

    def rest(self):
        self.mana += 10
        return f'{self.name} replenishes mana +10 {self.mana}'


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


hero_mage = Mage('<Rudeus>', 100, 1000)
print(hero_mage.actions())
