import unittest
from goldbach import *


class Goldbach_test(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertTrue(is_prime(7))

    def test_if_negative_is_prime(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-3))

    def test_gold_bach(self):
        self.assertEqual(goldbach(100), [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])

if __name__ == '__main__':
    unittest.main()
