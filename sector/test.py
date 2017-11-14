import unittest

from nilsson.start_examples.sector.model import Sector, SectorDirection


class TestSector(unittest.TestCase):

    def assertCasesEqual(self, cases):
        expected = [e for e, _ in cases]
        actual = [a for _, a in cases]

        self.assertEqual(expected, actual)

    def test_plus90_ccw(self):
        cases = [
            (True, Sector(90).contains(45)),
            (True, Sector(90).contains(45)),
            (False, Sector(180).contains(181)),
        ]
        self.assertCasesEqual(cases)

    def test_minus90_cw(self):
        cases = [
            (True, Sector(90, direction=SectorDirection.CW).contains(-45)),
            (True, Sector(90, direction=SectorDirection.CW).contains(-45)),
            (True, Sector(180, direction=SectorDirection.CW).contains(-180)),
            (True, Sector(360, direction=SectorDirection.CW).contains(-360)),
        ]
        self.assertCasesEqual(cases)


class TestSectorFactoryFunction(unittest.TestCase):
    def assertCasesEqual(self, cases):
        expected = [e for e, _ in cases]
        actual = [a for _, a in cases]

        self.assertEqual(expected, actual)

    def test_plus90_ccw(self):
        cases = [
            (True, Sector.ccw(90).contains(45)),
            (True, Sector.ccw(90).contains(45)),
            (False, Sector.ccw(180).contains(181)),
            (True, Sector.ccw(45, 90).contains(50)),
        ]
        self.assertCasesEqual(cases)

    def test_minus90_cw(self):
        cases = [
            (True, Sector.cw(90).contains(-45)),
            (True, Sector.cw(90).contains(-45)),
            (True, Sector.cw(180).contains(-180)),
            (True, Sector.cw(360).contains(-360))
        ]
        self.assertCasesEqual(cases)
