import unittest
from groupby import groupby


class Groupby_test(unittest.TestCase):
    def test_Groupby(self):
        self.assertEqual(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]), {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})
        self.assertEqual(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]), {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]})



if __name__ == '__main__':
    unittest.main()
