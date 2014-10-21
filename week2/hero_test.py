from hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.bron.name, "Bron")
        self.assertEqual(self.bron.health, 100)
        self.assertEqual(self.bron.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.bron.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(self.bron.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron.is_alive())

    def test_is_alive_with_dead(self):
        self.bron.health = 0
        self.assertFalse(self.bron.is_alive())

    def test_take_damage(self):
        self.bron.take_damage(50)
        self.assertEqual(self.bron.health, 50)

    def test_take_damage_max_dmg(self):
        self.bron.take_damage(200)
        self.assertEqual(self.bron.health, 0)
        self.bron.take_damage(20)
        self.assertEqual(self.bron.health, 0)

    def test_take_healing_on_dead(self):
        self.bron.health = 0
        self.assertFalse(self.bron.take_healing(100))

    def test_take_healing_above_maximum_health(self):
        self.bron.take_healing(1 + self.bron._MAX_HEALTH)
        self.assertTrue(self.bron.take_healing(1 + self.bron._MAX_HEALTH))
        self.assertEqual(self.bron.health, self.bron._MAX_HEALTH)

    def test_take_healing(self):
        self.bron.health = 20
        self.assertTrue(self.bron.take_healing(20))
        self.assertEqual(self.bron.health, 40)


if __name__ == '__main__':
    unittest.main()
