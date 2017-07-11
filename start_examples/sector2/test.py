import unittest


class TestSector(unittest.TestCase):

    def test_I_sector(self):
        I = Sector(0, 90)
        self.assertTrue(I.contains(0))
        self.assertTrue(I.contains(90))
        self.assertFalse(I.contains(90 + 1))
        self.assertFalse(I.contains(180))
        self.assertFalse(I.contains(180 + 90))
        self.assertFalse(I.contains(180 + 90 + 1))
        self.assertTrue(I.contains(360))
        self.assertTrue(I.contains(360 + 90))
        self.assertFalse(I.contains(360 + 90 + 1))


class Sector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def contains(self, angle):
        angle = self.rotate_360(angle)
        return angle <= self.b

    def rotate_360(self, angle):
        while angle >= 360:
            angle -= 360
        return angle
