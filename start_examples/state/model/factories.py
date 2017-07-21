from nilsson.start_examples.state.model.controller import TurnstileController
from nilsson.start_examples.state.model.state import Locked, Unlocked
from nilsson.start_examples.state.model.state_machine import StateMachine


class StateMachineFactory:

    LOCKED = Locked()
    UNLOCKED = Unlocked()

    @classmethod
    def new_turnstile_machine(cls):
        controller = TurnstileController()
        return StateMachine(controller)
