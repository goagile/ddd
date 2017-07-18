import unittest

from start_examples.po.msg.model import MsgCollection, Msg


class TestMsgCollection(unittest.TestCase):

    def test_eq(self):
        msg_collection1 = MsgCollection()
        msg_collection1.add_msg(id='Box', str='Ящик')

        msg_collection2 = MsgCollection()
        msg_collection2.add_msg(id='Box', str='Ящик')

        self.assertEqual(msg_collection1, msg_collection2)

    def test_count(self):
        expected = 1
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')

        result = msg_collection.count

        self.assertEqual(expected, result)

    def test_iter(self):
        box = Msg(id='Box')
        box.str = 'Ящик'
        expected = [box]
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')

        result = [msg for msg in msg_collection.msgs]

        self.assertEqual(expected, result)

    def test_put_and_get_single_msg(self):
        expected = 'Ящик'
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик')

        result = msg_collection.get_msg('Box').str

        self.assertEqual(expected, result)

    def test_add_msg_with_paths(self):
        expected = [
            '../modules/user/x.js:112',
            '../modules/user/x.js:300'
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик', paths=[
            '../modules/user/x.js:112',
            '../modules/user/x.js:300'
        ])

        box = msg_collection.get_msg('Box')
        result = [p for p in box.paths]

        self.assertEqual(expected, result)

    def test_put_and_get_plural_msg(self):
        expected = ['Ящик', 'Ящики']
        msg_collection = MsgCollection()
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик', 'Ящики'])

        result = msg_collection.get_msg('Box').strs

        self.assertEqual(expected, result)
