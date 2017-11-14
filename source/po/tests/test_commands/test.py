import unittest

from start_examples.po.config.commands import ParseMsgPath
from start_examples.po.msg_model.msg_collection import MsgCollection


class TestParseMsgPath(unittest.TestCase):

    def test_execute(self):
        expected = MsgCollection()
        expected.add_msg(id='Current', str='', paths=['../modules/user/x.js:300', '../modules/user/x.js:500'])
        command = ParseMsgPath('parse_path')
        line = '#: ../modules/user/x.js:300 ../modules/user/x.js:500'

        result = MsgCollection()
        command.execute(line, result)

        self.assertEqual(expected, result)
