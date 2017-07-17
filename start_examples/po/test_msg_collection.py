import unittest

from nilsson.start_examples.po.model import MsgCollection


class TestMsgCollection(unittest.TestCase):

    def test_count(self):
        expected = 1
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')

        result = msg_collection.count

        self.assertEqual(expected, result)

    def test_put_and_get_single_msg(self):
        expected = 'Ящик'
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')
        box = msg_collection.get_msg('Box')

        result = box.str

        self.assertEqual(expected, result)

    def test_put_and_get_plural_msg(self):
        expected = ['Ящик', 'Ящики']
        msg_collection = MsgCollection()
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик', 'Ящики'])
        box = msg_collection.get_msg('Box')

        result = box.strs

        self.assertEqual(expected, result)
