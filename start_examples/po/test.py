import unittest


class TestMsg(unittest.TestCase):

    def test_create_msg_with_id(self):
        expected = 'Box'
        msg = Msg('Box')

        result = msg.id

        self.assertEqual(expected, result)

    def test_get_str(self):
        expected = 'Ящик'
        msg = Msg('Box')
        msg.str = 'Ящик'

        result = msg.str

        self.assertEqual(expected, result)

    def test_add_path(self):
        expected = [
            '../modules/user/x.js:112',
            '../modules/user/x.js:300'
        ]
        msg = Msg('Box')
        msg.add_path('../modules/user/x.js:112')
        msg.add_path('../modules/user/x.js:300')

        result = [p for p in msg.paths]

        self.assertEqual(expected, result)


class Msg:

    def __init__(self, id):
        self.str = ''
        self.__id = id
        self.__paths = []

    @property
    def id(self):
        return self.__id

    def add_path(self, path: str):
        self.__paths.append(path)

    @property
    def paths(self):
        return iter(self.__paths)
