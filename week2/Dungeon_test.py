from Dungeon import Dungeon
import unittest
import os
from hero import Hero
from orc import Orc
from weapon import Weapon


class Test_dungeon(unittest.TestCase):

    def setUp(self):
        path = open("path.txt", "w")
        self.dung_map = """S.##......
#.##..###
#.###.###.
#.....###
###.####S"""
        path.write(self.dung_map)
        path.close()
        self.dungeon = Dungeon("path.txt")
        self.bron = Hero("Bron", 100, "DragonSlayer")
        self.orc = Orc("orc", 90, 1.4)
        self.bron.equip_weapon(Weapon("Mighty Axe", 25, 0.2))
        self.orc.equip_weapon(Weapon("basher", 16, 0.75))

    def test_dungeon_init(self):
        self.assertEqual(self.dungeon.map, self.dung_map)

    def test_spawn_hero(self):
        self.assertTrue(self.dungeon.spawn("hero", self.bron))
        self.dung_map = """H.##......
#.##..###
#.###.###.
#.....###
###.####S"""
        self.assertEqual(self.dungeon.map, self.dung_map)

    def test_spawn_hero_and_orc(self):
        self.assertTrue(self.dungeon.spawn("hero", self.bron))
        self.assertTrue(self.dungeon.spawn("orc", self.orc))
        self.dung_map = """H.##......
#.##..###
#.###.###.
#.....###
###.####O"""
        self.assertEqual(self.dungeon.map, self.dung_map)

    def test_spawn_no_free_start_postion(self):
        self.dungeon.spawn("hero", self.bron)
        self.dungeon.spawn("hero2", self.bron)
        self.assertFalse(self.dungeon.spawn("heroo", self.orc))

    def test_move_possible(self):
        self.dungeon.spawn("hero", self.bron)
        self.assertTrue(self.dungeon.move("hero", "right"))
        self.dung_map = """.H##......
#.##..###
#.###.###.
#.....###
###.####S"""
        self.assertEqual(self.dungeon.map, self.dung_map)

    def test_move_imposible(self):
        self.dungeon.spawn("hero", self.bron)
        self.assertFalse(self.dungeon.move("hero", "left"))
        self.dung_map = """H.##......
#.##..###
#.###.###.
#.....###
###.####S"""
        self.assertEqual(self.dungeon.map, self.dung_map)

    def test_move_fight(self):
        self.dungeon.map = """SS##......
#.##..###
#.###.###.
#.....###
###.####S"""
        self.dungeon.spawn("hero", self.bron)
        self.dungeon.spawn("orc", self.orc)
        self.dung_map = """.O##......
#.##..###
#.###.###.
#.....###
###.####S"""
        self.dungeon.move("hero", "right")
        self.assertEqual(self.dungeon.map, self.dung_map)

    def tearDown(self):
        os.remove("path.txt")


if __name__ == '__main__':
    unittest.main()
