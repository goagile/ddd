
class StatesBuilder:

    def __init__(self):
        self.states = []

    def __getattr__(self, item):
        if not item in self.__dict__:
            self.states.append(item)
            return
        self.__getattribute__(item)


class EventsBuilder:

    def __init__(self):
        self.events = []

    def __getattr__(self, item):
        if not item in self.__dict__:
            self.events.append(item)
            return
        self.__getattribute__(item)


class EventTransit:

    def __init__(self, states_builder):
        self.states_builder = states_builder

    def transit(self):
        return TransitTo()


class TransitTo:

    def __getattr__(self, item):
        if not item in self.__dict__:
            self.events.append(item)
            return
        self.__getattribute__(item)


class TransitionsBuilder:

    def __init__(self, states_builder, events_builder):
        self.transitions = []
        self.states_builder = states_builder
        self.events_builder = events_builder

    def __getattr__(self, item):
        if not item in self.__dict__:

            if item in self.events_builder.events:
                return EventTransit(self.states_builder)

            self.transitions.append(item)
            return
        self.__getattribute__(item)


class StateMachineConfig:

    def __init__(self):
        self.states_builder = StatesBuilder()
        self.events_builder = EventsBuilder()
        self.when = TransitionsBuilder(self.states_builder, self.events_builder)

    def run(self):
        self.configure(self.states_builder, self.events_builder, self.when)

    def configure(self, states, events, when):
        pass
