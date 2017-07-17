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

        t = Transition(start, event, waiting_msgstr)

        self.assertEqual('start', t.source.name)
        self.assertEqual('msgid_finded', t.trigger.name)
        self.assertEqual('waiting_msgstr', t.target.name)


class State:
    def __init__(self, name):
        self.name = name


class Transition:
    def __init__(self, source, trigger, target):
        self.source = source
        self.trigger = trigger
        self.target = target


class Event:

    def __init__(self, name):
        self.name = name
