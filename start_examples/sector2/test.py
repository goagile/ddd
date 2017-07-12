import unittest

from nilsson.start_examples.sector2.model import CcwSector


I = CcwSector(0, 90)
II_III_IV = CcwSector(90, 0)


class TestCcwSector(unittest.TestCase):

    def test_I_sector_positive_angle(self):
        sector = I
        self.assertTrue(sector.contains(0))
        self.assertTrue(sector.contains(90))
        self.assertFalse(sector.contains(90 + 1))
        self.assertFalse(sector.contains(180))
        self.assertFalse(sector.contains(180 + 90))
        self.assertFalse(sector.contains(180 + 90 + 1))
        self.assertTrue(sector.contains(360))
        self.assertTrue(sector.contains(360 + 90))
        self.assertFalse(sector.contains(360 + 90 + 1))

    def test_I_sector_negative_angle(self):
        sector = I
        self.assertFalse(sector.contains(-1))
        self.assertFalse(sector.contains(-90))
        self.assertFalse(sector.contains(-180))
        self.assertFalse(sector.contains(-180 - 89))
        self.assertTrue(sector.contains(-180 - 90))
        self.assertTrue(sector.contains(-360))
        self.assertFalse(sector.contains(-360 - 1))

    def test_II_III_IV_sector_positive_angle(self):
        sector = II_III_IV
        self.assertTrue(sector.contains(0))
        self.assertTrue(sector.contains(90))
        self.assertFalse(sector.contains(90 - 1))
        self.assertFalse(sector.contains(0 + 1))
        self.assertTrue(sector.contains(180))
        self.assertTrue(sector.contains(180 + 90))
        self.assertTrue(sector.contains(360))
    #     self.assertTrue(sector.contains(360 + 90))
    #     self.assertFalse(sector.contains(360 + 90 + 1))
