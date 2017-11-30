"""

    >>> store = EventStore()
    >>> event = DomainEvent(email='xxx@gmail.com')
    >>> event_id = store.add(event)
    >>> event_id
    10
    >>> se = store.get_event_by_id(10)
    >>> se
    StoredEvent(event_id=10, email=xxx@gmail.com)


"""


class DomainEvent:

    def __init__(self, email):
        self.email = email


class StoredEvent:

    def __init__(self, event_id, email):
        self.event_id = event_id
        self.email = email

    def __repr__(self):
        return 'StoredEvent(event_id={}, email={})'.format(self.event_id, self.email)


class EventStore:

    ids = iter([10, 20, 30])
    events = {}

    def add(self, event):
        event_id = self.next_id()
        self.events[event_id] = StoredEvent(
            event_id,
            email=event.email
        )
        return event_id

    def get_event_by_id(self, event_id):
        return self.events.get(event_id)

    def next_id(self):
        return next(self.ids)
