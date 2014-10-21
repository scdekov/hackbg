from fight import Fight
import unittest
from orc import Orc
from hero import Hero
from weapon import Weapon


class Test_Fight(unittest.TestCase):
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
        self.assertTrue(self.orc.health == 0 or self.hero.health == 0)

    def test_flip_coin(self):
        results = set()
        for i in range(100):
            results.add(self.fight._flip_coin())
        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    unittest.main()

