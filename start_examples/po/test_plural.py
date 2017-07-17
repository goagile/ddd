import unittest

from nilsson.start_examples.po.model import MsgPlural


boxes = MsgPlural(id='Box', id_plural='Boxes')


class TestMsgPlural(unittest.TestCase):

    def test_is_plural(self):
        self.assertTrue(boxes.is_plural)

    def test_create_msg_with_id(self):
        self.assertEqual('Box', boxes.id)
        self.assertEqual('Boxes', boxes.id_plural)

    def test_add_str(self):
        expected = [
            'Ящик',
            'Ящики'
        ]
        boxes.add_str('Ящик')
        boxes.add_str('Ящики')

        result = [s for s in boxes.strs]

        self.assertEqual(expected, result)

    def test_add_path(self):
        expected = [
            '../modules/user/x.js:112',
            '../modules/user/x.js:300'
        ]
        boxes.add_path('../modules/user/x.js:112')
        boxes.add_path('../modules/user/x.js:300')

        result = [p for p in boxes.paths]

        self.assertEqual(expected, result)
