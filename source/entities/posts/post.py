"""

Нельзя создать пустой Post

    >>> p = Post(None, None)
    Traceback (most recent call last):
    ...
    AssertionError

Заполняет заголовок и содержание

    >>> content = 'Some info about writing the post'
    >>> title = 'My new post'
    >>> p = Post(content, title)

    >>> str(p.status)
    'UNPUBLISHED'

"""


class DateTimeImmutable:

    def __init__(self):
        pass


class Status:

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value

    @classmethod
    def published(cls):
        return Status('PUBLISHED')

    @classmethod
    def unpublished(cls):
        return Status('UNPUBLISHED')


class Post:

    def __init__(self, content, title):
        self.__content = None
        self.__title = None
        self.__set_content(content)
        self.__set_title(title)
        self.__status = None
        self.unpublish()
        self.__create_at = DateTimeImmutable()
        self.__publish_at = None

    def __set_content(self, content):
        assert content
        self.__content = content

    def __set_title(self, title):
        assert title
        self.__title = title

    def __set_create_at(self, create_at: DateTimeImmutable):
        assert self.__is_valid_date(create_at)
        self.__create_at = create_at

    def __set_publish_at(self, publish_at: DateTimeImmutable):
        assert self.__is_valid_date(publish_at)
        self.__publish_at = publish_at

    def __is_valid_date(self, create_at: DateTimeImmutable):
        return True

    @property
    def status(self):
        return self.__status

    def publish(self):
        self.__status = Status.published()

    def unpublish(self):
        self.__status = Status.unpublished()
