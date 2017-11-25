"""

Таблица
=======

Создание и доступ
-----------------

Подключаем таблицу

    >>> from tablo.tablo import Tablo

Создание таблицы (с указанием заголовков)

    >>> headers = 'X Y Z A B'.split()
    >>> tablo = Tablo(headers)

Добавление строки в таблицу

    >>> row = '@', 4, 2.1, False, 'Нет'
    >>> tablo.append_row(row)

Доступ к строке по индексу, доступ к ячейке по имени столбца

    >>> row = tablo[0]
    >>> row.X, row.Y, row.Z, row.A, row.B
    ('@', 4, 2.1, False, 'Нет')

Доступ к строке по индексу, доступ к ячейке по индексу столбца

    >>> row = tablo[0]
    >>> row[0], row[1], row[2], row[3], row[4]
    ('@', 4, 2.1, False, 'Нет')

Добавление строки в таблицу

    >>> row = '&', 22, 5.03, True, 'Да'
    >>> tablo.append_row(row)

Доступ к столбцу по индексу строки

    >>> column_X = tablo.X
    >>> column_X[0], column_X[1]
    ('@', '&')

Перебор строк и доступ к данным строки

    >>> for row in tablo:
    ...     row.data
    ['@', 4, 2.1, False, 'Нет']
    ['&', 22, 5.03, True, 'Да']

Перебор строк и столбцов

    >>> for row in tablo:
    ...     [col for col in row]
    ['@', 4, 2.1, False, 'Нет']
    ['&', 22, 5.03, True, 'Да']


Ошибки
======

Добавление сложного типа в ячейку

    >>> row = ('@', 4, 2.1, False, ['invalid', 'data'])
    >>> tablo.append_row(row)
    Traceback (most recent call last):
        ...
    ValueError: '['invalid', 'data']' Invalid Primitive type

Доступ к несуществующей строке

    >>> column_X[10]
    Traceback (most recent call last):
      ...
    AttributeError: '10' Invalid row index

Доступ к несуществующему атрибуту по имени столбца

    >>> row = tablo[0]
    >>> row.G
    Traceback (most recent call last):
      ...
    AttributeError: 'G' Invalid column name

"""
