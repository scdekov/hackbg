import unittest
from weapon import Weapon


class Test_Weapon(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon("Mighty Axe", 25, 0.2)

    def test_init_weapon(self):
        self.assertEqual(self.weapon.type, "Mighty Axe")
        self.assertEqual(self.weapon.damage, 25)
        self.assertEqual(self.weapon.critical_strike_percent, 0.2)

    def test_init_weapon_wrong_crit_chance(self):
        with self.assertRaises(ValueError):
            axe = Weapon("axe", 5, 4)
        with self.assertRaises(ValueError):
            axe = Weapon("axe", 5, -1)

    def test_critical_hit(self):
        results = set()
        for i in range(1000):
            results.add(self.weapon.critical_hit())
        self.assertEqual(len(results), 2)



if __name__ == '__main__':
    unittest.main()
