import unittest

from nilsson.start_examples.po.state_machine.model import Controller, StateMachine, State, Transition, Event, \
    PrintCommand

waiting_new_line = State('waiting_new_line')
new_line_finded = Event('new_line_finded')
waiting_new_line.add_command('print')

waiting_paths = State('waiting_paths')
paths_finded = Event('paths_finded')
waiting_new_line.add_command('print')

waiting_msgid = State('waiting_msgid')
msgid_finded = Event('msgid_finded')
waiting_new_line.add_command('print')

waiting_msgstr = State('waiting_msgstr')
msgstr_finded = Event('msgstr_finded')
waiting_new_line.add_command('print')

waiting_new_line.add_transition(target=waiting_paths, event=new_line_finded)
waiting_paths.add_transition(target=waiting_msgid, event=paths_finded)
waiting_msgid.add_transition(target=waiting_msgstr, event=msgid_finded)
waiting_msgstr.add_transition(target=waiting_new_line, event=msgstr_finded)


class Test(unittest.TestCase):

    def setUp(self):
        command_channel = {
            'print': PrintCommand('print')
        }
        self.machine = StateMachine(waiting_new_line)
        self.controller = Controller(self.machine, command_channel)

    def fire(self, event_name):
        self.controller.handle(event_name)

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
