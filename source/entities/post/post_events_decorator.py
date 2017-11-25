"""

Проверим, что список событий пуст

    >>> DomainEventsListener.events
    []

Публикуем пост

    >>> p = Post(post_id=1, title='Как связать события предметной области с сущностями')
    >>> p.status
    'Draft'

    >>> p.publish()
    >>> p.status
    'Published'

Проверяем, что мы добавили событие

    >>> DomainEventsListener.events
    [PostPublished(post_id='1')]

Снимаем пост с публикации

    >>> p.unpublish()
    >>> p.status
    'Draft'

Проверяем, что событие домена добавлено

    >>> DomainEventsListener.events
    [PostPublished(post_id='1'), PostUnpublished(post_id='1')]

"""


class DomainEventsListener:
    events = []

    @classmethod
    def publish(cls, event):
        cls.events.append(event)


class DomainEvent:

    def __init__(self, name):
        self.name = name


class PostPublished(DomainEvent):

    def __init__(self, post_id):
        super().__init__(name=self.__class__.__name__)
        self.post_id = post_id

    def __repr__(self):
        return "{}(post_id='{}')".format(self.__class__.__name__, self.post_id)


class PostUnpublished(PostPublished):
    pass


def pub(event):
    def inner(decorated_function):
        def decorator(post):
            decorated_function(post)
            e = event(post.post_id)
            DomainEventsListener.publish(e)
        return decorator
    return inner


class Post:

    def __init__(self, post_id, title):
        self.post_id = post_id
        self.title = title
        self.status = 'Draft'

    @pub(event=PostPublished)
    def publish(self):
        self.status = 'Published'

    @pub(event=PostUnpublished)
    def unpublish(self):
        self.status = 'Draft'
