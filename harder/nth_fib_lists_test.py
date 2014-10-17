import unittest
from nth_fib_lists import nth_fib_lists


class Nth_fib_lists_test(unittest.TestCase):

    def test_nth_fib_lists(self):
        self.assertEquals(nth_fib_lists([1], [2], 1), [1])
        self.assertEquals(nth_fib_lists([1, 2], [1, 3], 3), [1, 2, 1, 3])

    def test_nth_fib_with_negative_n(self):
        self.assertFalse(nth_fib_lists([1, 2], [1, 3], -1))

if __name__ == '__main__':
    unittest.main()
