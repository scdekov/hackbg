import unittest
from prepare_meal import prepare_meal


class Prepare_meal_test(unittest.TestCase):

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(5), "eggs")
        self.assertEqual(prepare_meal(27), "spam spam spam ")
        self.assertEqual(prepare_meal(45), "spam spam and eggs")
        self.assertEqual(prepare_meal(7), "")


if __name__ == '__main__':
    unittest.main()
