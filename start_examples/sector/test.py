import unittest


class SectorDirection:
    CW = 'Clockwise'
    CCW = 'CounterClockwise'


class Test(unittest.TestCase):

    def assertCasesEqual(self, cases):
        expected = [e for e, _ in cases]
        actual = [a for _, a in cases]

        self.assertEqual(expected, actual)

    def test_plus90_ccw(self):
        cases = [
            (True, Sector(stop=90).contains(45)),
            (True, Sector(start=90).contains(45)),
            (False, Sector(180).contains(181)),
        ]
        self.assertCasesEqual(cases)

    def test_minus90_cw(self):
        cases = [
            (True, Sector(stop=90, direction=SectorDirection.CW).contains(-45)),
            (True, Sector(start=90, direction=SectorDirection.CW).contains(-45)),
            (True, Sector(stop=180, direction=SectorDirection.CW).contains(-180)),
            (True, Sector(360, direction=SectorDirection.CW).contains(-360)),
        ]
        self.assertCasesEqual(cases)

    # def test(self):
    #     result = sector_ccw(90).contains(45)
    #
    #     self.assertTrue(result)

#
# def sector_ccw(angle):
#     return Sector(start=angle, direction='ccw')


class Sector:

    def __init__(self, start=0, stop=0, direction=SectorDirection.CCW):
        self.direction = direction
        self._start = start
        self._stop = stop
        self.start = start
        self.stop = stop

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if self.direction == SectorDirection.CW:
            self._start = -value
        else:
            self._start = value

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        if self.direction == SectorDirection.CW:
            self._stop = -value
        else:
            self._stop = value

    def contains(self, angle):
        left = min(self.start, self.stop)
        right = max(self.start, self.stop)
        return bool(left <= angle <= right)
