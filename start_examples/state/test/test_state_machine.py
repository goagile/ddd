import unittest

from nilsson.start_examples.state.model.factories import StateMachineFactory


class TestStateMachine(unittest.TestCase):

    def setUp(self):
        self.machine = StateMachineFactory.new_turnstile_machine()

    def test_create_state_machine(self):
        self.assertEqual(StateMachineFactory.LOCKED, self.machine.state)

    def test_transition_locked_coin_unlocked(self):
        self.machine.coin()

        self.assertMachineController(StateMachineFactory.UNLOCKED, 'is_coin')

    def test_transition_locked_turn_locked(self):
        self.machine.turn()

        self.assertMachineController(StateMachineFactory.LOCKED, 'is_turn')

    def assertMachineController(self, state, controller_attr):
        self.assertEqual(state, self.machine.state)

        controller = self.machine.controller
        attr = getattr(controller, controller_attr)
        self.assertTrue(attr)
