import unittest

from count_words import count_words


class Count_words_test(unittest.TestCase):
    def test_count_words(self):
        test_arr = ["heaSS", "ASAS", "A", "A"]
        result = {"heaSS": 1, "ASAS": 1, "A": 2}
        self.assertEqual(result, count_words(test_arr))

    def test_if_no_words(self):
        test_arr = []
        result = {}
        self.assertEqual(result, count_words(test_arr))


if __name__ == '__main__':
    unittest.main()
