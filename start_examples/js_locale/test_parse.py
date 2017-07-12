import re
import unittest


QUOTES = r'(?:\'|\")'
TR = r'TR(\1)'
SYMBOLS = r'- :_;.,?!'
RU = r'А-Яа-я'


def wrap_in_quotes(text):
    return '({}{}{})'.format(QUOTES, text, QUOTES)


CONST = re.compile(wrap_in_quotes(r'['+SYMBOLS+RU+']+'))
IGNORE = re.compile(wrap_in_quotes('['+SYMBOLS+']+'))


class TestInsertTr(unittest.TestCase):

    def test_insert_tr(self):
        expected = 'var x = [TR("Имя"), TR("Фамилия")]; '
        text = 'var x = ["Имя", "Фамилия"]; '

        result = insert_tr_to(text, CONST, TR, IGNORE)

        self.assertEqual(expected, result)

    def test_insert_tr_2(self):
        expected = 'var x = [TR("Имя"), TR("Фамилия по"), ":", "-"]; '
        text = 'var x = ["Имя", "Фамилия по", ":", "-"]; '

        result = insert_tr_to(text, CONST, TR, IGNORE)

        self.assertEqual(expected, result)


def insert_tr_to(text, pattern, sub, ignore):
    parts = pattern.split(text)
    result = [find(part, pattern, sub, ignore) for part in parts]
    return ''.join(result)


def find(text, pattern, sub, ignore):
    if pattern.match(text) and not ignore.match(text):
        return pattern.sub(sub, text)
    return text
