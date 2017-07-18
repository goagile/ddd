

class Transition:

    def __init__(self, source, trigger, target, commands=None):
        self.source = source
        self.trigger = trigger
        self.target = target
        self.command_names = [] if not commands else commands

    def add_command(self, command_name):
        self.command_names.append(command_name)
