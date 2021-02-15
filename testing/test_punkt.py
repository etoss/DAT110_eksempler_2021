import unittest, math
from testing.punkt_properties import Punkt

class TestPunkt(unittest.TestCase):
    def test_y_koordinat(self):
        p1 = Punkt(5, 5)
        p2 = Punkt(0, 9)
        self.assertEqual(5, p1.y_koordinat)
        self.assertEqual(9, p2.y_koordinat)
        p1.y_koordinat = 15
        self.assertEqual(15, p1.y_koordinat)
        self.assertEqual(9, p2.y_koordinat)

    def test_x_koordinat(self):
        p1 = Punkt(5, 5)
        p2 = Punkt(2, 9)
        self.assertEqual(5, p1.x_koordinat)
        self.assertEqual(2, p2.x_koordinat)
        p1.x_koordinat = 3
        self.assertEqual(3, p1.x_koordinat)
        self.assertEqual(2, p2.x_koordinat)
        with self.assertRaises(ValueError):
            p1.x_koordinat = -5
        with self.assertRaises(ValueError):
            p1.x_koordinat = -2

    def test_r(self):
        p1 = Punkt(3, 4)
        p2 = Punkt(2, 9)
        self.assertAlmostEqual(5.0, p1.r, 5)
        self.assertAlmostEqual(9.219544, p2.r, 5)

    def test_theta(self):
        p1 = Punkt(3, 4)
        p2 = Punkt(2, 9)
        forventet_verdi = math.acos(p1.x_koordinat/p1.r)
        self.assertAlmostEqual(forventet_verdi, p1.theta, 5)
        forventet_verdi = math.acos(p2.x_koordinat/p2.r)
        self.assertAlmostEqual(forventet_verdi, p2.theta, 5)


if __name__ == "__main__":
    unittest.main()
