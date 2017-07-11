import unittest

from nilsson.start_examples.sector2.model import Sector


I = Sector(0, 90)


class TestSector(unittest.TestCase):

    def test_I_sector_positive_angle(self):
        self.assertTrue(I.contains(0))
        self.assertTrue(I.contains(90))
        self.assertFalse(I.contains(90 + 1))
        self.assertFalse(I.contains(180))
        self.assertFalse(I.contains(180 + 90))
        self.assertFalse(I.contains(180 + 90 + 1))
        self.assertTrue(I.contains(360))
        self.assertTrue(I.contains(360 + 90))
        self.assertFalse(I.contains(360 + 90 + 1))

    def test_I_sector_negative_angle(self):
        self.assertFalse(I.contains(-1))
        self.assertFalse(I.contains(-90))
        self.assertFalse(I.contains(-180))
        self.assertFalse(I.contains(-180 - 89))
        self.assertTrue(I.contains(-180 - 90))
        self.assertTrue(I.contains(-360))
        self.assertFalse(I.contains(-360 - 1))
