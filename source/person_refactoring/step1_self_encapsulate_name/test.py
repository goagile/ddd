import unittest
from datetime import datetime


class Test(unittest.TestCase):
    def test(self):
        p = Person('Jim')

        self.assertEqual('Jim', p.name)

    def test_strange_children(self):
        p = Person('Jim')

        p.children = [
            1, 'A', datetime.year, float(2/4)
        ]

        self.assertEqual([1, 'A', datetime.year, float(2/4)], p.children)


class Person:
    def __init__(self, name):
        self.__name = name
        self.birthdate = datetime.now()
        self.children = []

    @property
    def name(self):
        return self.__name

    def how_old(self):
        if self.birthdate < datetime.now():
            years = datetime.now().year - self.birthdate.year
            if datetime.now().timetuple().tm_yday < self.birthdate.timetuple().tm_yday:
                years -= 1
            return years
        else:
            return 0
