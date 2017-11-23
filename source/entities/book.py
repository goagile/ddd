"""

    >>> isbn = '1234567890X'
    >>> title = 'Python programming'
    >>> book = Book(isbn, title)

    >>> str(book.isbn)
    '1234567890X'

    >>> book.isbn.__class__.__name__
    'ISBN'

"""


class ISBN:

    def __init__(self, isbn_str: str):
        self.isbn_str = isbn_str

    def __str__(self):
        return '{}'.format(self.isbn_str)


class Book:

    def __init__(self, isbn, title):
        self.__isbn = isbn
        self.title = title

    @property
    def isbn(self):
        return ISBN(self.__isbn)
