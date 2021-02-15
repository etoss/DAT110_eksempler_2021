import unittest
from testing.karakterer import karakter


class TestKarakter(unittest.TestCase):
    def test_karakter(self):
        self.assertEqual("A", karakter(98))
        self.assertEqual("A", karakter(90))
        self.assertEqual("B", karakter(89))
        self.assertEqual("B", karakter(83))
        self.assertEqual("B", karakter(80))
        self.assertEqual("C", karakter(79))
        self.assertEqual("C", karakter(65))
        self.assertEqual("C", karakter(60))
        self.assertEqual("D", karakter(59))
        self.assertEqual("D", karakter(57))
        self.assertEqual("D", karakter(50))
        self.assertEqual("E", karakter(49))
        self.assertEqual("E", karakter(42))
        self.assertEqual("E", karakter(40))
        self.assertEqual("F", karakter(39))
        self.assertEqual("F", karakter(25))
