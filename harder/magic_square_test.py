import unittest
from magic_square import magic_square


class Magic_square_test(unittest.TestCase):

    def test_magic_square(self):
        self.assertTrue(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
        self.assertFalse(magic_square([[1,2,3], [4,5,6], [7,8,9]]))


if __name__ == '__main__':
    unittest.main()
