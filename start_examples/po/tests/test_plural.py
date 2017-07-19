import unittest

from start_examples.po.msg_model.msg_plural import MsgPlural

boxes = MsgPlural(id='Box', id_plural='Boxes')


class TestMsgPlural(unittest.TestCase):

    def test_is_id_empty(self):
        boxes1 = MsgPlural(id='', id_plural='Boxes')
        boxes2 = MsgPlural(id='Box', id_plural='')

        self.assertTrue(boxes1.is_id_empty)
        self.assertTrue(boxes2.is_id_empty)

    def test_eq(self):
        boxes1 = MsgPlural(id='Box', id_plural='Boxes')
        boxes2 = MsgPlural(id='Box', id_plural='Boxes')
        self.assertEqual(boxes1, boxes2)

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
