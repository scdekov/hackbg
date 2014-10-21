from fight import Fight
import unittest
from orc import Orc
from hero import Hero
from weapon import Weapon


class Test_Fight(unittest_TestCase):
    def setUp(self):
        self.orc = Orc("orc", 90, 1.4)
        self.hero = Hero("hero", 100, "DragonSlayer")
        self.hero.equip_weapon(Weapon("Mighty Axe", 25, 0.2))
        self.orc.equip_weapon(Weapon("basher", 16, 0.75))
        self.fight = Fight(self.hero, self.orc)

    def test_fight_init(self):
        self.assertEqual(self.fight.orc, self.orc)
        self.assertEqual(self.fight.hero, self.hero)

    def test_simulate_fight(self):
        self.fight.simulate_fight()

