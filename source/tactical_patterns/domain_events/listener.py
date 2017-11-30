"""

Канал сообщений (Слушатель событий)
===================================

Создаем нового пользователя.
Операция создания публикует событие UserRegistered в
канале DomainEventsListener

    >>> user = User('xxx@email.com')

Проверяем, что событие попало в канал

    >>> DomainEventsListener.domain_events
    {1: UserRegistered(email=xxx@email.com)}

"""


class UserRegistered:

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return 'UserRegistered(email={})'.format(self.email)


class DomainEventsListener:

    domain_events = {}

    @classmethod
    def publish(cls, domain_event):
        event_id = 1
        cls.domain_events[event_id] = domain_event


class User:

    def __init__(self, email):
        self.email = email
        self.publish_event(email)

    @classmethod
    def publish_event(cls, email):
        DomainEventsListener.publish(
            UserRegistered(email)
        )
