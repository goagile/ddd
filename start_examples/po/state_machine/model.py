

class Controller:

    def __init__(self, machine, commands):
        self.machine = machine
        self.commands = commands
        self.current_state = machine.start

    def handle(self, event_name):
        if self.current_state.has_transition(event_name):
            self.transition_to(self.current_state.target_state(event_name))

    def transition_to(self, target):
        self.current_state = target


class StateMachine:

    def __init__(self, start):
        self.start = start


class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, target, event):
        self.transitions[event.name] = Transition(self, event, target)

    def has_transition(self, event_name):
        return bool(event_name in self.transitions)

    def target_state(self, event_name):
        return self.transitions.get(event_name).target


class Transition:
    def __init__(self, source, trigger, target):
        self.source = source
        self.trigger = trigger
        self.target = target


class Event:

    def __init__(self, name):
        self.name = name
