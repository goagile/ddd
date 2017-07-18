from nilsson.start_examples.po.state_machine_model.transition import Transition


class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, target, event, commands=None):
        self.transitions[event.name] = Transition(self, event, target, commands)

    def has_transition(self, event_name):
        return bool(event_name in self.transitions)

    def target_state(self, event_name):
        return self.transitions.get(event_name).target

    def transition_commands(self, event_name):
        return self.transitions.get(event_name).command_names
