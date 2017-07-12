

class CcwSector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def contains(self, angle):
        angle = self.rotate_360(angle)
        result = bool(self.a <= angle <= self.b)
        return result

    def rotate_360(self, angle):
        while angle >= 360:
            angle -= 360
        while angle < 0:
            angle += 360
        if self.b < self.a:
            self.b += 360
            if angle == 0:
                angle = 360
        return angle
