"""

Издатель
========

Создаем хранилище Событий

    >>> store = EventStore()

Создаем подписчика на события

    >>> subscriber = PersistDomainEventSubscriber(store)

Подписываем подписчика на канал

    >>> DomainEventPublisher.subscribe(subscriber)

Создаем событие

    >>> event = DomainEvent()

Публикуем событие в канале

    >>> DomainEventPublisher.publish(event)

Проверяем, что событие попало в Хранилище

    >>> store.events
    [DomainEvent]

"""

import abc


class DomainEvent:

    def __repr__(self):
        return 'DomainEvent'


class DomainEventSubscriber(abc.ABC):

    @abc.abstractmethod
    def is_subscribed_to(self, event: DomainEvent):
        pass

    @abc.abstractmethod
    def handle(self, event: DomainEvent):
        pass


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


class EventStore:

    events = []

    def append(self, event: DomainEvent):
        self.events.append(event)


class PersistDomainEventSubscriber(DomainEventSubscriber):

    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, event: DomainEvent):
        self.event_store.append(event)

    def is_subscribed_to(self, event: DomainEvent):
        return True
