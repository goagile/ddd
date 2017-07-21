import unittest

from nilsson.start_examples.state.model.factories import StateMachineFactory


class TestStateMachine(unittest.TestCase):

    def test_create_state_machine(self):
        locked = StateMachineFactory.LOCKED

        machine = StateMachineFactory.new_turnstile_machine()

        result = machine.state
        self.assertEqual(locked, result)

    def test_transition_locked_coin_unlocked(self):
        unlocked = StateMachineFactory.UNLOCKED
        machine = StateMachineFactory.new_turnstile_machine()

        machine.coin()

        result = machine.state
        self.assertEqual(unlocked, result)
        self.assertTrue(machine.controller.is_coin)
