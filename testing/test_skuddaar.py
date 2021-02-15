import unittest
from testing.skuddaar import skuddaar


class TestSkuddaar(unittest.TestCase):
    def test_skuddaar(self):
        self.assertTrue(skuddaar(2000))
        self.assertTrue(skuddaar(1600))
        self.assertFalse(skuddaar(1900))
        self.assertFalse(skuddaar(2100))
        self.assertTrue(skuddaar(2020))
        self.assertTrue(skuddaar(2004))
        self.assertTrue(skuddaar(1996))
        self.assertFalse(skuddaar(2018))
        self.assertFalse(skuddaar(2001))
        self.assertFalse(skuddaar(1998))
