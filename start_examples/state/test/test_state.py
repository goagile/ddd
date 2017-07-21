import unittest

from nilsson.start_examples.state.model.factories import StateMachineFactory


class TestState(unittest.TestCase):

    def test_states_are_equal(self):
        locked = StateMachineFactory.LOCKED
        state = StateMachineFactory.LOCKED
        self.assertEqual(locked, state)
