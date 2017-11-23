"""

Имя должно быть не пустым

    >>> Username('')
    Traceback (most recent call last):
        ...
    AssertionError: Имя пустое

Имя не должно быть короче 5-ти символов

    >>> Username('абвг')
    Traceback (most recent call last):
        ...
    AssertionError: Имя слишком короткое

Имя не должно быть длиннее 10-ти символов

    >>> Username('Петров-Васечкин')
    Traceback (most recent call last):
        ...
    AssertionError: Имя слишком длинное


Валидные имена

    >>> Username('Бернард')
    >>> Username('Кот789_')

"""

import re


class Username:

    min_len = 5
    max_len = 10
    format = re.compile('^[a-zA-Zа-яА-Я0-9_]+$')

    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__assert_not_empty(value)
        self.__assert_not_too_short(value)
        self.__assert_not_too_long(value)
        self.__assert_valid_format(value)
        self.__name = value

    def __assert_not_empty(self, name):
        assert name, 'Имя пустое'

    def __assert_not_too_short(self, name):
        assert len(name) >= self.min_len, 'Имя слишком короткое'

    def __assert_not_too_long(self, name):
        assert len(name) < self.max_len, 'Имя слишком длинное'

    def __assert_valid_format(self, name):
        assert self.format.match(name), 'Некорректный формат имени'
