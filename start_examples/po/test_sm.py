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


class State:

    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, target, event):
        t = Transition(self, event, target)
        self.transitions.append(t)


class Transition:
    def __init__(self, source, trigger, target):
        self.source = source
        self.trigger = trigger
        self.target = target


class Event:

    def __init__(self, name):
        self.name = name
