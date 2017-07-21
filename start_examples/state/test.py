import unittest


class TestStateMachine(unittest.TestCase):

    def test_is_coin_false_by_default(self):
        controller = TurnstileController()

        result = controller.is_coin

        self.assertFalse(result)

    def test_is_coin_by_controller_coin(self):
        controller = TurnstileController()

        controller.coin()

        result = controller.is_coin
        self.assertTrue(result)

    def test_create_state_machine(self):
        locked = Locked()
        controller = TurnstileController()

        machine = StateMachine(controller)

        result = machine.state
        self.assertEqual(locked, result)

    def test_states_are_equal(self):
        locked = Locked()
        state = Locked()
        self.assertEqual(locked, state)

    def test_transition_locked_coin_unlocked(self):
        unlocked = Unlocked()
        controller = TurnstileController()
        machine = StateMachine(controller)

        machine.coin()

        result = machine.state
        self.assertEqual(unlocked, result)
        self.assertTrue(controller.is_coin)


class State:

    def __init__(self):
        self.name = self.__class__.__name__

    def __eq__(self, other):
        return bool(self.name == other.name)


class Locked(State):
    pass


class Unlocked(State):
    pass


class StateMachine:

    def __init__(self, controller):
        self.state = Locked()
        self.controller = controller

    def coin(self):
        self.state = Unlocked()
        self.controller.coin()


class TurnstileController:

    def __init__(self):
        self.is_coin = False

    def coin(self):
        self.is_coin = True
