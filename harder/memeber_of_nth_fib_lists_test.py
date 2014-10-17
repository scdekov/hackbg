import unittest
from member_of_nth_fib_lists import member_of_nth_fib_lists


class Member_of_nth_fib_lists_test(unittest.TestCase):

    def test_member_of_nth_fib_lists(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertTrue(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))


if __name__ == '__main__':
    unittest.main()
