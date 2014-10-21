from orc import Orc
import unittest
from weapon import Weapon


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("orc", 90, 1.4)

    def test_orc_init(self):
        self.assertEqual(self.orc.name, "orc")
        self.assertEqual(self.orc.health, 90)
        self.assertEqual(self.orc.berserk_factor, 1.4)

    def test_orc_init_weak_orc(self):
        weak_orc = Orc("orc", 20, 0.2)
        self.assertEqual(weak_orc.name, "orc")
        self.assertEqual(weak_orc.health, 20)
        self.assertEqual(weak_orc.berserk_factor, 1)

    def test_orc_init_strong_orc(self):
        strong_orc = Orc("orcc", 200, 20)
        self.assertEqual(strong_orc.name, "orcc")
        self.assertEqual(strong_orc.health, 200)
        self.assertEqual(strong_orc.berserk_factor, 2)

    def test_get_health(self):
        self.assertEqual(self.orc.get_health(), 90)

    def test_is_alive(self):
        self.assertTrue(self.orc.is_alive())

    def test_is_alive_with_dead(self):
        self.orc.health = 0
        self.assertFalse(self.orc.is_alive())

    def test_take_damage(self):
        self.orc.take_damage(50)
        self.assertEqual(self.orc.health, 40)

    def test_take_damage_max_dmg(self):
        self.orc.take_damage(200)
        self.assertEqual(self.orc.health, 0)
        self.orc.take_damage(20)
        self.assertEqual(self.orc.health, 0)

    def test_take_healing_on_dead(self):
        self.orc.health = 0
        self.assertFalse(self.orc.take_healing(100))

    def test_take_healing_above_maximum_health(self):
        self.orc.take_healing(1 + self.orc._MAX_HEALTH)
        self.assertTrue(self.orc.take_healing(1 + self.orc._MAX_HEALTH))
        self.assertEqual(self.orc.health, self.orc._MAX_HEALTH)

    def test_take_healing(self):
        self.orc.health = 20
        self.assertTrue(self.orc.take_healing(20))
        self.assertEqual(self.orc.health, 40)

    def test_attack(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.orc.equip_weapon(weapon)
        if self.orc.weapon.critical_hit():
            self.assertEqual(self.orc.attack(), self.orc.weapon.damage * self.orc.berserk_factor *2)
        else:
            self.assertEqual(self.orc.attack(), self.orc.weapon.damage * self.orc.berserk_factor)

if __name__ == '__main__':
    unittest.main()
