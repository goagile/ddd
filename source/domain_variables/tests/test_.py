import unittest

from domain_variables.current.complex_value import Ic
import cmath


class Test(unittest.TestCase):

    def test_x(self):
        i1 = Ic.from_rect(re=2, im=5)
        print(i1)

    # def test_(self):
    #     i1 = Ic.from_polar(mod=12, ang=90)
    #     print(i1)
