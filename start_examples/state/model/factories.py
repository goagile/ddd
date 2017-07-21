from nilsson.start_examples.state.model.controller import TurnstileController
from nilsson.start_examples.state.model.state import Locked, Unlocked
from nilsson.start_examples.state.model.state_machine import TurnstileStateMachine


class StateMachineFactory:

    LOCKED = Locked()
    UNLOCKED = Unlocked()

    @classmethod
    def new_turnstile_machine(cls):
        return TurnstileStateMachine(
            initial_state=cls.LOCKED,
            controller=TurnstileController())
