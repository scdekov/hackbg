import unittest
from simplify_fraction import *


class Simplify_fraction_test(unittest.TestCase):

    def test_simplify_fracion(self):
        self.assertEqual(simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(simplify_fraction((4, 10)), (2, 5))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))



if __name__ == '__main__':
    unittest.main()


