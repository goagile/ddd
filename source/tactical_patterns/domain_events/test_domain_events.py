import abc
import unittest


class TestDomainEventPublisher(unittest.TestCase):

    def test_is_should_publish_user_registered_event(self):
        # создаем подписчика
        subscriber = SpySubscriber()
        # подписываем его на канал
        DomainEventPublisher.subscribe(subscriber)
        user_id = UserId('user-1-0-0')

        # создаем пользователя
        user = User(user_id, 'xxx@gmail.com', 123)

        # проверяем, что сообщение попало в канал
        self.assertUserRegisteredEventPublisged(subscriber, user_id)

    def assertUserRegisteredEventPublisged(self, subscriber, user_id):
        self.assertIsInstance(subscriber.event, UserRegistered)
        self.assertEqual(subscriber.event.user_id, user_id)


class UserId:

    def __init__(self, user_id: str):
        self.user_id = user_id


class User:

    def __init__(self, user_id: UserId, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password

        DomainEventPublisher.publish(UserRegistered(user_id))


class DomainEvent:

    def __repr__(self):
        return 'DomainEvent'


class UserRegistered(DomainEvent):

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'UserRegistered'


class DomainEventSubscriber(abc.ABC):

    def __init__(self):
        self.event = None

    @abc.abstractmethod
    def is_subscribed_to(self, event: DomainEvent):
        pass

    @abc.abstractmethod
    def handle(self, event: DomainEvent):
        pass


class SpySubscriber(DomainEventSubscriber):

    def is_subscribed_to(self, event: DomainEvent):
        return True

    def handle(self, event: DomainEvent):
        self.event = event


class DomainEventPublisher:

    subscribers = []

    @classmethod
    def subscribe(self, subscriber: DomainEventSubscriber):
        self.subscribers.append(subscriber)

    @classmethod
    def publish(self, event: DomainEvent):
        for subscriber in self.subscribers:
            if subscriber.is_subscribed_to(event):
                subscriber.handle(event)
