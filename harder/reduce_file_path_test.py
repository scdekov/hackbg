import unittest
from reduce_file_path import reduce_file_path


class Reduce_file_path_test(unittest.TestCase):

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/"), "/")
        self.assertEqual(reduce_file_path("/srv/../"), "/")
        self.assertEqual(reduce_file_path("/../"), "/")
        self.assertEqual(reduce_file_path("//////////////"), "/")
        self.assertEqual(reduce_file_path("/srv/www/htdocs/wtf"), "/srv/www/htdocs/wtf")


if __name__ == '__main__':
    unittest.main()
