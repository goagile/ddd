import unittest
import re


class Test(unittest.TestCase):

    def test(self):
        expected = '(555баобаб555)'
        text = '(баобаб)'

        result = re.sub(r'([А-Яа-я]+)', r'555\g<1>555', text)

        self.assertEqual(expected, result)
        print(result)
