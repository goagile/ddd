import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.config_po_states import waiting_new_line
from start_examples.po.state_machine_model.controller import Controller
from start_examples.po.state_machine_model.state_machine import StateMachine


class PrintCommand:
    def __init__(self, name):
        self.name = name

    def execute(self, line):
        print(line)


class Test(unittest.TestCase):

    def setUp(self):
        command_channel = {
            'print': PrintCommand('print')
        }
        self.machine = StateMachine(waiting_new_line)
        self.controller = Controller(self.machine, command_channel, MsgCollection())

    def fire(self, event_name):
        self.controller.handle(event_name, '')

    def assertCurrentState(self, state):
        self.assertEqual(state, self.controller.current_state.name)

    def test_new_line_finded(self):
        self.fire('new_line_finded')
        self.assertCurrentState('waiting_paths')

        self.fire('paths_finded')
        self.assertCurrentState('waiting_msgid')

        self.fire('msgid_finded')
        self.assertCurrentState('waiting_msgstr')

        self.fire('msgstr_finded')
        self.assertCurrentState('waiting_new_line')
