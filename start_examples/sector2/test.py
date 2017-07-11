import unittest


class TestSector(unittest.TestCase):

    def test(self):
        self.assertTrue(Sector(0, 90).contains(45))
        self.assertTrue(Sector(0, 90).contains(180))
        self.assertTrue(Sector(0, 90).contains(270))


class Sector:
    pass
