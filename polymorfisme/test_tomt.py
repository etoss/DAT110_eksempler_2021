import unittest
from polymorfisme.tomt import Tomt


class MockRegion:
    def __init__(self, test_areal):
        self.test_areal = test_areal

    def areal(self):
        return self.test_areal


class TestTomt(unittest.TestCase):
    def test_kvadratmeterpris(self):
        tomt = Tomt(1, "Jan Johansen", MockRegion(200), 200000)
        self.assertAlmostEqual(1000.0, tomt.kvadratmeterpris(), 6)
        tomt = Tomt(1, "Jan Johansen", MockRegion(500), 300000)
        self.assertAlmostEqual(600.0, tomt.kvadratmeterpris(), 6)
