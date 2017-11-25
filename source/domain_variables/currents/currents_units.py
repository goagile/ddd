import operator

from domain_variables.base.units import Unit


class A(Unit):

    @staticmethod
    def kA(value):
        return operator.truediv(value, 1e3), kA()


class kA(Unit):

    @staticmethod
    def A(value):
        return operator.mul(value, 1e3), A()


class Units:
    A = A()
    kA = kA()
