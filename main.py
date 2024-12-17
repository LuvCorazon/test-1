

from abc import ABC, abstractmethod

import random



class Hero(ABC):
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #safety attribute
        self._luck = random.randint(1, 100)
        #private attribute
        self.__crit_dmg = random.randint(1, 100)

    def __heal_hp(self):
        return random.randint(1, 100)

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f' {self.name} heal hp \n Health:{self.hp}.')

    def greetings(self):
        return print(f'Hello! {self.name}\n My lvl: {self.lvl}')

    def status(self):
        return print(f'{self.lvl}\n {self.hp}')

    def attck(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name}  crit dmg')
        else:
            return print(f'{self.name}  basic dmg')

    def defence(self):
        if self._luck >= 20:
            return print(f'{self.name}  succcesfuly defend')
        else:
            return print(f'{self.name}  got damage')

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass



# hero = Hero('Messi', 100, 1)
# hero.attck()
# hero.defence()
# hero.rest()

class ShieldHero(Hero):
    def __init__(self, name, hp, lvl, aura=0):
        super().__init__(name, hp, lvl)
        self.aura = aura

    def defence(self):
        if self._luck >= 70:
            return print(f'{self.name}  succcesfuly defend')
        else:
            self.aura += 100
            return print(f'{self.name}  got damage')

    def unique_attack(self):
        if self.aura >= 10:
            return print(f'{self.name}  unique attack')
        else:
            return print(f"{self.name} doesn't have enough aura")

    def unique_scream(self):
        if self.aura >= 10:
            return print(f'{self.name}  unique scream')

naofumi = ShieldHero('naofumi', 100, 1, )
naofumi.attck()
naofumi.defence()
naofumi.unique_attack()

