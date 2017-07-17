import unittest

from nilsson.start_examples.po.model import Msg


box = Msg(id='Box')


class TestMsg(unittest.TestCase):

    def test_eq(self):
        box1 = Msg(id='Box')
        box2 = Msg(id='Box')
        self.assertEqual(box1, box2)

    def test_is_plural(self):
        self.assertFalse(box.is_plural)

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
