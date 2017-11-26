"""

    >>> DomainEventListener.events
    []

    >>> user = User(1, 'Петр Петрович')

    >>> DomainEventListener.events
    [UserRegistered(user_id='1')]

"""


class DomainEventListener:
    events = []

    @classmethod
    def publish(cls, event):
        cls.events.append(event)


class UserRegistered:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "UserRegistered(user_id='{}')".format(self.user_id)


def publish(event):
    def inner(*args):
        def func(*args):
            e = event(args[1])
            DomainEventListener.publish(e)
        return func
    return inner


class User:

    @publish(event=UserRegistered)
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
