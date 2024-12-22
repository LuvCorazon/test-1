from abc import ABC, abstractmethod

import random

class Hero(ABC):
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck = random.randint (0, 100)
        self.__crit_dmg = random.randint (0,100)
        self.__random_action = random.randint(1,3)

    def greetings(self):
        return print(f'Hello {self.name} \n my lvl:')

    def status(self):
        return print (f'{self.lvl}\n hp:{self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} crit damage')
        else:
            return print (f'{self.name}basic dmg')

    def protect(self):
        if self._luck >= 20:
            return print(f'{self.name} succesfuly defend')
        else:
            return print(f"{self.name} can't defend")

    def __heal_hp(self):
        return random.randint (1,100)


    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} rest and heals hp\n hp:{self.hp}')




    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def scream(self):
        pass



    @abstractmethod
    def action(self):
        pass



# hero = Hero('goku', 100, 1)
# print (hero.attack())
# print(hero.status())
# print (hero.rest())


class Jester(Hero):


    def __init__(self, name, hp, lvl, aura = 0):
        super().__init__(name, hp, lvl)
        self.aura = aura
        self.__random_action = random.randint(1, 3)


    def protect(self):
        if self._luck >= 80:
            return print(f'{self.name} succesfuly defend')
        else:
            self.aura += 100
            return print(f"{self.name} can't defend")

    def unique_attack(self):
        if self.aura >= 10:
            return print(f'{self.name} use unique attack')
        else:
            return print(f'{self.name} not have enough aura')

    def scream(self):
        if self.aura >= 1:
            return print(f'{self.name} use scream')

    def action(self):
        if self.__random_action == 1:
            return print(f'{self.name} {self.attack()}')
        if self.__random_action == 2:
            return print(f'{self.name} {self.protect()}')
        if self.__random_action == 3:
            return print(f'{self.name} {self.rest()}')





cap = Jester('cap', 200, 1)
print (cap.action())


