import unittest
from unique_words_count import unique_words_count


class Unique_words_count_test(unittest.TestCase):

    def test_unique_words_count(self):
        self.assertEqual(unique_words_count(["apple", "banana", "apple", "pie"]), 3)
        self.assertEqual(unique_words_count(["python", "python", "python", "ruby"]), 2)
        self.assertEqual(unique_words_count(["HELLO!"] * 10), 1)


if __name__ == '__main__':
    unittest.main()
