from hero import Hero
from orc import Orc
import random


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def _flip_coin(self):
        return int(random.random() >= 0.5)

    def simulate_fight(self):
        coin = self._flip_coin()
        while(self.hero.is_alive() and self.orc.is_alive()):
            if coin == 0:
                crr_dmg = self.hero.attack()
                print("{} attack {} with {}dmg !".format(self.hero.known_as(), self.orc.name, crr_dmg))
                self.orc.take_damage(crr_dmg)
                crr_dmg = self.orc.attack()
                print("{} attack {} with {}dmg !".format(self.orc.name, self.hero.known_as(), crr_dmg))
                self.hero.take_damage(crr_dmg)
            else:
                crr_dmg = self.orc.attack()
                print("{} attack {} with {}dmg !".format(self.orc.name, self.hero.known_as(), crr_dmg))
                self.hero.take_damage(crr_dmg)
                crr_dmg = self.hero.attack()
                print("{} attack {} with {}dmg !".format(self.hero.known_as(), self.orc.name, crr_dmg))
                self.orc.take_damage(crr_dmg)
        if (self.hero.is_alive()):
            print("{} is the WINNER ! {} is dead!".format(self.hero.known_as(), self.orc.name))
        else:
            print("{} is the WINNER ! {} is dead!".format(self.orc.name, self.hero.known_as()))



