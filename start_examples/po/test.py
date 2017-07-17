import unittest

from nilsson.start_examples.po.model import Msg


box = Msg(id='Box')


class TestMsg(unittest.TestCase):

    def test_create_msg_with_id(self):
        expected = 'Box'

        result = box.id

        self.assertEqual(expected, result)

    def test_get_str(self):
        expected = 'Ящик'
        box.str = 'Ящик'

        result = box.str

        self.assertEqual(expected, result)

    def test_add_path(self):
        expected = [
            '../modules/user/x.js:112',
            '../modules/user/x.js:300'
        ]
        box.add_path('../modules/user/x.js:112')
        box.add_path('../modules/user/x.js:300')

        result = [p for p in box.paths]

        self.assertEqual(expected, result)
