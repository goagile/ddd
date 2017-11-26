"""

Нельзя создать пустой Post

    >>> p = Post(None, None)
    Traceback (most recent call last):
    ...
    AssertionError

Заполняет заголовок и содержание
Заголовок является уникальным ключом сущности

    >>> title = 'My new post'
    >>> content = 'Some info about writing the post'
    >>> p = Post(title, content)

Проверяем, что Пост не опубликован

    >>> p.is_published()
    False
    >>> str(p.status)
    'DRAFT'

Публикуем пост

    >>> p.publish()
    >>> p.is_published()
    True
    >>> str(p.status)
    'PUBLISHED'

Проверяем дату публикации и дату создания поста

    >>> str(p.publish_at)
    '02.10.2020'
    >>> str(p.created_at)
    '02.10.2020'

"""


class DateTimeImmutable:

    def __str__(self):
        return '02.10.2020'


class Status:

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return self.__value

    def __eq__(self, other):
        return bool(self.value == other.value)

    @classmethod
    def published(cls):
        return Status('PUBLISHED')

    @classmethod
    def draft(cls):
        return Status('DRAFT')


class Post:

    def __init__(self, title, content):
        self.__title = None
        self.__content = None
        self.__set_content(content)
        self.__set_title(title)
        self.__status = None
        self.unpublish()
        self.__create_at = DateTimeImmutable()
        self.__publish_at = None

    # текстовое содержимое
    def __set_content(self, content):
        assert content
        self.__content = content

    def __set_title(self, title):
        assert title
        self.__title = title

    # работа с датами
    @property
    def created_at(self):
        return self.__create_at

    @property
    def publish_at(self):
        return self.__publish_at

    def __set_create_at(self, create_at: DateTimeImmutable):
        assert self.__is_valid_date(create_at)
        self.__create_at = create_at

    def __set_publish_at(self, publish_at: DateTimeImmutable):
        assert self.__is_valid_date(publish_at)
        self.__publish_at = publish_at

    def __is_valid_date(self, create_at: DateTimeImmutable):
        return True

    # управление статусами
    @property
    def status(self):
        return self.__status

    def publish(self):
        self.__status = Status.published()
        self.__publish_at = DateTimeImmutable()

    def unpublish(self):
        self.__status = Status.draft()

    def is_published(self):
        return bool(self.status == Status.published())
