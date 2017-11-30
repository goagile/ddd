"""

    >>> notification_service = NotificationService()

"""


class EventStore:
    pass


class MessageTracker:
    pass


class MessageProducer:
    pass


class NotificationService:

    def __init__(
        self,
        store: EventStore,
        tracker: MessageTracker,
        producer: MessageProducer
    ):
        self.store = store
        self.tracker = tracker
        self.producer = producer

    def publish_notifications(self, exchange_name) -> int:
        message_id = self.tracker.get_most_recent_published_message_id(exchange_name)
        notifications = self.get_unpublished_notifications(message_id)
        if not notifications:
            return 0

        self.producer.open(exchange_name)
