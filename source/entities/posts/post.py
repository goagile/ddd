"""

    >>> content = 'xxx'
    >>>
    >>> p = Post()

"""


class DateTimeImmutable:

    def __init__(self):
        pass


class Post:

    def __init__(self, content, title):
        self.__content = None
        self.__title = None
        self.__set_content(content)
        self.__set_title(title)
        self.unpublish()
        self.create_at = DateTimeImmutable()

    def __set_content(self, content):
        self.__content = content

    def __set_title(self, title):
        self.__title = title

    def unpublish(self):
        pass
