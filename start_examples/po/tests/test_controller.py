import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.config_po_statemachine import waiting_new_line
from start_examples.po.state_machine_model.controller import Controller
from start_examples.po.state_machine_model.state_machine import StateMachine


class Test(unittest.TestCase):

    def setUp(self):
        command_channel = {}
        self.machine = StateMachine(waiting_new_line)
        self.controller = Controller(self.machine, command_channel, MsgCollection())

    def fire(self, event_name):
        self.controller.handle(event_name, '')

    def assertCurrentState(self, state):
        self.assertEqual(state, self.controller.current_state.name)

    def test_single(self):
        self.fire('new_line_finded')
        self.assertCurrentState('waiting_paths')

        self.fire('paths_finded')
        self.assertCurrentState('waiting_msgid')

        self.fire('msgid_finded')
        self.assertCurrentState('waiting_msgstr')

        self.fire('msgstr_finded')
        self.assertCurrentState('waiting_paths')

    def test_plural(self):
        self.fire('new_line_finded')
        self.assertCurrentState('waiting_paths')

        self.fire('paths_finded')
        self.assertCurrentState('waiting_msgid')

        self.fire('paths_finded')
        self.assertCurrentState('waiting_msgid')

        self.fire('msgid_finded')
        self.assertCurrentState('waiting_msgstr')

        self.fire('msgid_plural_finded')
        self.assertCurrentState('waiting_msgstr_0')

        self.fire('msgstr_0_finded')
        self.assertCurrentState('waiting_msgstr_1')

        self.fire('msgstr_1_finded')
        self.assertCurrentState('waiting_msgstr_2')

        self.fire('msgstr_2_finded')
        self.assertCurrentState('waiting_new_line')
