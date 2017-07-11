import unittest


class TestSector(unittest.TestCase):

    def test_I_sector(self):
        I = Sector(0, 90)
        self.assertTrue(I.contains(0))
        self.assertTrue(I.contains(45))
        self.assertTrue(I.contains(90))
        self.assertFalse(I.contains(180))
        self.assertFalse(I.contains(270))
        self.assertFalse(I.contains(360))


class Sector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def contains(self, angle):
        return angle <= self.b
