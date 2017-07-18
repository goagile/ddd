from start_examples.po.state_machine_model.transition import Transition


class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.command_names = []

    def add_command(self, command_name):
        self.command_names.append(command_name)

    def add_transition(self, target, event):
        self.transitions[event.name] = Transition(self, event, target)

    def has_transition(self, event_name):
        return bool(event_name in self.transitions)

    def target_state(self, event_name):
        return self.transitions.get(event_name).target
