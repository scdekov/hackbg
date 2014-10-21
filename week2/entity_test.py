from entity import Entity
import unittest
from weapon import Weapon


class Test_Entity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity("ent", 50)

    def test_has_weapon(self):

        self.entity.weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertTrue(self.entity.has_weapon())

    def test_equip_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        self.assertEqual(self.entity.weapon, weapon)

    def test_attack_if_have_weapon_no_crit(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        self.assertEqual(self.entity.attack(), self.entity.weapon.damage)

    def test_attack_if_have_weapon_crit(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        if self.entity.weapon.critical_hit():
            self.assertEqual(self.entity.attack(), self.entity.weapon.damage * 2)
        else:
            self.assertEqual(self.entity.attack(), self.entity.weapon.damage)

    def test_attack_if_havnt_weapon(self):
        self.assertEqual(self.entity.attack(), 0)




if __name__ == '__main__':
    unittest.main()


