import unittest


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


class Controller:

    def __init__(self, machine, commands):
        self.machine = machine
        self.commands = commands
        self.current_state = machine.start

    def handle(self, event_name):
        if self.current_state.has_transition(event_name):
            self.transition_to(self.current_state.target_state(event_name))

    def transition_to(self, target):
        self.current_state = target


class StateMachine:

    def __init__(self, start):
        self.start = start


class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, target, event):
        self.transitions[event.name] = Transition(self, event, target)

    def has_transition(self, event_name):
        return bool(event_name in self.transitions)

    def target_state(self, event_name):
        return self.transitions.get(event_name).target


class Transition:
    def __init__(self, source, trigger, target):
        self.source = source
        self.trigger = trigger
        self.target = target


class Event:

    def __init__(self, name):
        self.name = name
