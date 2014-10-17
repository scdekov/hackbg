import unittest
from is_an_bn import is_an_bn


class Is_an_bn_test(unittest.TestCase):

    def test_with_empty_word(self):
        self.assertFalse(is_an_bn(""))

    def test_with_odd_len_word(self):
        self.assertFalse(is_an_bn("aab"))

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("bbbaaa"))


if __name__ == '__main__':
    unittest.main()
