from nilsson.start_examples.state.model.state import Locked, Unlocked


class StateMachine:

    LOCKED = Locked()
    UNLOCKED = Unlocked()

    def __init__(self, controller):
        self.state = StateMachine.LOCKED
        self.controller = controller

    def coin(self):
        self.state = StateMachine.UNLOCKED
        self.controller.coin()
