

class SectorDirection:
    CW = 'Clockwise'
    CCW = 'CounterClockwise'


class Sector:

    def __init__(self, start=0, stop=0, direction=SectorDirection.CCW):
        self.direction = direction
        self.__start = self.__set_angle(start)
        self.__stop = self.__set_angle(stop)
        self.__min = min(self.__start, self.__stop)
        self.__max = max(self.__start, self.__stop)

    @staticmethod
    def ccw(start=0, stop=0):
        return Sector(start, stop, direction=SectorDirection.CCW)

    @staticmethod
    def cw(start=0, stop=0):
        return Sector(start, stop, direction=SectorDirection.CW)

    def __set_angle(self, value):
        return -value if self.is_cw() else value

    def is_cw(self):
        return bool(SectorDirection.CW == self.direction)

    def is_ccw(self):
        return bool(SectorDirection.CCW == self.direction)

    def contains(self, angle):
        return bool(self.__min <= angle <= self.__max)
