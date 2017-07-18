

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
        self.execute_commands(line)
        self.current_state = target

    def execute_commands(self, line):
        for command_name in self.current_state.command_names:
            command = self.command_channel.get(command_name)
            if command:
                command.execute(line, self.msg_collection)
