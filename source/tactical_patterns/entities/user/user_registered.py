"""

    >>> DomainEventListener.events
    []

    >>> user = User(user_id=1, name='Петр Петрович')

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


class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        # оповещаем предметную область о том, что новый пользователь создан
        event = UserRegistered(user_id=self.user_id)
        DomainEventListener.publish(event)
