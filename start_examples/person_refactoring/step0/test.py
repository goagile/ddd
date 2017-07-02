import unittest
from datetime import datetime


class Test(unittest.TestCase):
    def test(self):
        p = Person()
        p.name = 'Jim'

        self.assertEqual('Jim', p.name)


class Person:
    def __init__(self):
        self.name = ''
        self.birthdate = datetime.now()
        self.children = []

    def how_old(self):
        if self.birthdate < datetime.now():
            years = datetime.now().year - self.birthdate.year
            if datetime.now().timetuple().tm_yday < self.birthdate.timetuple().tm_yday:
                years -= 1
            return years
        else:
            return 0
