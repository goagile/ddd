

class ParsePathCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        path = 'xxx'
        if not msg_collection.has_msg('Current'):
            msg_collection.add_msg('Current')
        msg_collection.get_msg('Current')
        msg_collection.add_path_to('Current', path)


class Controller:

    def __init__(self, machine, command_channel, msg_collection):
        self.machine = machine
        self.command_channel = command_channel
        self.current_state = machine.start
        self.msg_collection = msg_collection

    def handle(self, event_name, line):
        if self.current_state.has_transition(event_name):
            target = self.current_state.target_state(event_name)
            self.transition_to(target, line)

    def transition_to(self, target, line):
        self.current_state = target
        for command_name in self.current_state.command_names:
            command = self.command_channel.get(command_name)
            if command:
                command.execute(line, self.msg_collection)


class StateMachine:

    def __init__(self, start):
        self.start = start


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


class Transition:
    def __init__(self, source, trigger, target):
        self.source = source
        self.trigger = trigger
        self.target = target


class Event:

    def __init__(self, name):
        self.name = name
