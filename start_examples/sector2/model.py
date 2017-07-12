

class CcwSector:
    def __init__(self, a, b):
        if a == b:
            raise ValueError('Counter Clockwise sector from {} to {} is not contains any angle'.format(a, b))
        self.a = a
        self.b = b

    def contains(self, angle):
        angle = self.rotate_360(angle)
        a = self.a
        b = self.b

        if b < a:
            b += 360
            if angle == 0:
                angle = 360
        elif a < b:
            if angle == 360:
                angle = 0

        result = bool(a <= angle <= b)
        return result

    def rotate_360(self, angle):
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        return angle
