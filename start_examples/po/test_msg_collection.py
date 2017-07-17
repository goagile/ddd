import unittest

from nilsson.start_examples.po.model import MsgCollection


class TestMsgCollection(unittest.TestCase):

    def test_count(self):
        expected = 1
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')

        result = msg_collection.count

        self.assertEqual(expected, result)

    def test_get_msg(self):
        expected = 'Ящик'
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')
        box = msg_collection.get_msg('Box')

        result = box.str

        self.assertEqual(expected, result)
