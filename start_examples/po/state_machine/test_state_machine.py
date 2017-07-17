import unittest

from nilsson.start_examples.po.state_machine.model import Controller, StateMachine, State, Transition, Event


class Test(unittest.TestCase):

    def test_event(self):
        e = Event('init')

        self.assertEqual('init', e.name)

    def test_state(self):
        start = State('start')

        self.assertEqual('start', start.name)

    def test_transition(self):
        start = State('start')
        event = Event('msgid_finded')
        waiting_msgstr = State('waiting_msgstr')

        form_start_to_waiting_msgstr = Transition(start, event, waiting_msgstr)

        self.assertEqual('start', form_start_to_waiting_msgstr.source.name)
        self.assertEqual('msgid_finded', form_start_to_waiting_msgstr.trigger.name)
        self.assertEqual('waiting_msgstr', form_start_to_waiting_msgstr.target.name)

    def test_add_transition_to_state(self):
        waiting_msgstr = State('waiting_msgstr')
        msgstr_finded = Event('msgstr_finded')
        waiting_msgstr.add_transition(waiting_msgstr, msgstr_finded)

        result = len(waiting_msgstr.transitions)

        self.assertEqual(1, result)

    def test_(self):
        start = State('start')
        machine = StateMachine(start)
        msgid_finded = Event('msgid_finded')
        waiting_msgstr = State('waiting_msgstr')
        start.add_transition(waiting_msgstr, event=msgid_finded)
        controller = Controller(machine, [])

        controller.handle('msgid_finded')

        self.assertEqual(waiting_msgstr, controller.current_state)
