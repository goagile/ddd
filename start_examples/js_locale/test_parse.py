import re
import unittest


QUOTES = r'(?:\'|\")'

ru = re.compile(QUOTES + r'([А-Яа-я]+)' + QUOTES)


class Test(unittest.TestCase):

    def test_findall(self):
        expected = ['Имя', 'Фамилия']
        text = "var columns = ['Имя', 'Фамилия'];"

        result = findall(text)

        self.assertEqual(expected, result)

    def test_split(self):
        expected = ['var x = ', 'Пуск', '; ']
        text = "var x = 'Пуск'; "

        result = split(text)

        print(result)

        self.assertEqual(expected, result)

    # def test_insert_tr(self):



def findall(text):
    result = ru.findall(text)
    return result


def split(text):
    result = ru.split(text)
    return result


def split_str(text):
    splitted = ru.split(text)
    find = findall(text)

    result = []
    count = len(splitted)
    for i in range(count):
        result.append(splitted[i])
        if find and i < count - 1:
            result.extend(find)

    return result
