"""

Создаем службу оповещения

    >>> connection = AMPQStreamConnection('localhost', 5672, 'guest', 'guest')
    >>>> RabbitMQMessageProducer(connection)


    >>> store = None
    >>> tracker = None
    >>> producer = None
    >>> notification_service = NotificationService(store, tracker, producer)

    >>> exchange_name = 'XXX'
    >>> number_of_notofications = notification_service.publish_notifications(exchange_name)


"""


class PublishedMessage:
    def __init__(self, exchange_name, message_id):
        self.exchange_name = exchange_name
        self.message_id = message_id

    def update_most_recent_published_message_id(self, max_id):
        pass


class EventStore:

    def get_all_stored_events_since(self, message_id):
        return []


class MessageTracker:

    def get_most_recent_published_message_id(self, exchange_name):
        return None

    def track_most_recent_published_messages(self, exchange_name, notification):
        if not notification:
            return
        max_id = notification.event_id

        published_mesage = self.find_one_by_exchange_name(exchange_name)
        if not published_mesage:
            published_mesage = PublishedMessage(exchange_name, max_id)
        published_mesage.update_most_recent_published_message_id(max_id)
        # self.persist(published_mesage)

    def find_one_by_exchange_name(self, exchange_name):
        return None


class MessageProducer:

    def open(self, exchange_name):
        pass

    def close(self, exchange_name):
        pass

    def send(self,
             exchange_name,
             serialized_notification,
             notification_name,
             event_id,
             occured_on):
        pass


class RabbitMQMessaging:

    def __init__(self, connection):
        self.connection = connection
        self.channel = None

    def connect(self, exchange_name):
        if not self.channel:
            return

        channel = self.connection.channel
        channel.exchange_declare(exchange_name, 'fanout', False, True, False)
        channel.queue_declare(exchange_name, False, True, False, False)
        channel.queue_bind(exchange_name, exchange_name)

        self.channel = channel

    def channel(self, exchange_name):
        self.connect(exchange_name)
        return self.channel


    def close(self, exchange_name):
        self.channel.close()
        self.connection.close()


class AMPQMessage:

    def __init__(self, notification_message, config):
        self.notification_meaage = notification_message
        self.config = config


class RabbitMQMessageProducer(RabbitMQMessaging):

    def send(
        self,
        exchange_name,
        notification_message,
        notification_type,
        notification_id,
        notification_occured_on
    ):
        self.channel(exchange_name).basic_publish(
            AMPQMessage(
                notification_message,
                {
                    'type': notification_type,
                    'timestamp': notification_occured_on.time_stamp,
                    'message_id': notification_id
                }
            ),
            exchange_name
        )



class NotificationSerializer:

    def __init__(self):
        pass

    def serialize(self, notification):
        return {}


class NotificationService:

    serializer = NotificationSerializer()

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

        published_messages = 0
        last_published_notification = None
        for notification in notifications:
            last_published_notification = self.publish(exchange_name, notification)
            published_messages += 1
        self.tracker.track_most_recent_published_messages(exchange_name, last_published_notification)

        self.producer.close(exchange_name)

    def get_unpublished_notifications(self, message_id):
        resullt = self.store.get_all_stored_events_since(message_id)
        return resullt

    def publish(self, exchange_name, notification):
        self.producer.send(
            exchange_name,
            self.serializer.serialize(notification),
            notification.name,
            notification.event_id,
            notification.occured_on
        )

        return notification

