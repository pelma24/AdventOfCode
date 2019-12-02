import unittest
from day9 import do

class Day9Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(do(10, 1618), 8317)

    def test2(self):
        self.assertEqual(do(13, 7999), 146373)

    def test3(self):
        self.assertEqual(do(17, 1104), 2764)

    def test4(self):
        self.assertEqual(do(21, 6111), 54718)

    def test5(self):
        self.assertEqual(do(30, 5807), 37305)

if __name__ == '__main__':
    unittest.main()
