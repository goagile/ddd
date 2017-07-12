import re
import unittest

from nilsson.start_examples.tr.model import TRWrapper

QUOTES = r'(?:\'|\")'
SYMBOLS = r'- :_;.,?!'
RU = r'А-Яа-я'


def wrap_in_quotes(text):
    return '({}{}{})'.format(QUOTES, text, QUOTES)


CONST = re.compile(wrap_in_quotes(r'['+SYMBOLS+RU+']+'))
TR = r'TR(\1)'
IGNORE = re.compile(wrap_in_quotes('['+SYMBOLS+']+'))


wrapper = TRWrapper(CONST, TR, IGNORE)


class TestTRWrapper(unittest.TestCase):

    def test_insert_tr(self):
        expected = 'var x = [TR("Имя"), TR("Фамилия")]; '
        text = 'var x = ["Имя", "Фамилия"]; '

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)

    def test_insert_tr_2(self):
        expected = 'var x = [TR("Имя, Отчество"), TR("Фамилия по"), ":", "-"]; '
        text = 'var x = ["Имя, Отчество", "Фамилия по", ":", "-"]; '

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)
